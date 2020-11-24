import dataclasses
import datetime


@dataclasses.dataclass()
class TestObject:
    add_date: datetime.datetime
    name: str

