from ezreal import db
from ezreal.tests import BaseTestCase
from ezreal.article.models import Tag
from tests.base import env
from tests.base.base import BaseEnv
from tests.sample_data import tag


env_list_1 = BaseEnv(
    [
        tag.tag_1,
        tag.tag_2
    ]
)

env_list_2 = BaseEnv(
    [
        tag.tag_1,
        tag.tag_2,
        tag.tag_3
    ]
)


class TestSampleData(BaseTestCase):

    @env.with_env(env_list_1)
    def test_create_sample_data_1(self):
        self.assertEqual(db.session.query(Tag).filter().count(), 2)

    @env.with_env(env_list_2)
    def test_create_sample_data_2(self):
        self.assertEqual(db.session.query(Tag).filter().count(), 3)
