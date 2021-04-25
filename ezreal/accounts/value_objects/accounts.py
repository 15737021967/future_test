import dataclasses
from ezreal.common import value_object


@dataclasses.dataclass()
class AccountValueObject(value_object.BaseValueObject):
    user_id: int
