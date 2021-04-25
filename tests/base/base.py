from typing import List
from ezreal import db
from ezreal.common.models import BaseModel
from sqlalchemy.engine import reflection

INSPECTOR = reflection.Inspector.from_engine(db.engine)


ALLOW_CREATE = False


class SampleData:
    def __init__(self, model, data):
        self.model = model
        self.data: dict = data
        self.instance = None

    def create_instance(self):
        if self.instance:
            return self.instance.id

        self.instance = self.model()

        columns = INSPECTOR.get_columns(self.model.__tablename__)
        for column in columns:
            column_name = column.get('name')
            column_nullable = column.get('nullable')
            column_type = column.get("type")
            if column_name == 'id':
                continue
            if column_name in self.data:
                data = self.data.get(column_name)
                if isinstance(column_type, db.Integer) and \
                        isinstance(data, SampleData):
                    fk = data.create_instance()
                    setattr(self.instance, column_name, fk)
                else:
                    setattr(self.instance, column_name, data)
            if column_name not in self.data and column_nullable is False:
                raise Exception(f'{self.model.__name__.lower()} 的非空字段 {column_name} 不能为空')

        db.session.add(self.instance)
        db.session.flush()

        return self.instance.id

    def relation_model(self):
        result = [self]
        for key, value in self.data.items():
            if isinstance(value, SampleData):
                result.extend(value.relation_model())
        return result

    def init_instance(self):
        self.instance = None


class BaseEnv:

    def __init__(self, sample_data_list: List[SampleData]):
        self.sample_data_list = sample_data_list
        self.relation = []
        self.init_relation()

    def init_relation(self):
        for item in self.sample_data_list:
            self.relation.extend(item.relation_model())
        self.relation = set(self.relation)

    def __enter__(self):
        for ins in self.sample_data_list:
            ins.create_instance()
        db.session.commit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        for ins in self.relation:
            ins.init_instance()
        model_list = BaseModel.__subclasses__()
        for model in model_list:
            db.session.query(model).delete()
        db.session.commit()
