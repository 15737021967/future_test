import datetime
import json

from feature.tests import BaseTestCase
from feature.common.utils import response_encoder
from feature.common.value_objects.test_object import TestObject


class TestCommon(BaseTestCase):

    def test_response_encode(self):
        test_data = TestObject(
            add_date=datetime.datetime.now(),
            name="time"
        )
        result = json.loads(response_encoder.encode(test_data))
        self.assertEqual(result["name"], "time")
