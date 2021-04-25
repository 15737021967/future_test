import datetime
import json

from ezreal.tests import BaseTestCase
from ezreal.common.utils import response_encoder
from ezreal.common.value_objects.test_object import TestObject


class TestCommon(BaseTestCase):

    def test_response_encode(self):
        test_data = TestObject(
            add_date=datetime.datetime.now(),
            name="time"
        )
        result = json.loads(response_encoder.encode(test_data))
        self.assertEqual(result["name"], "time")
