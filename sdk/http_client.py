import requests

from typing import Dict


class BaseRequests:

    @classmethod
    def parse_response(cls, response: requests.Response):
        if response.status_code != 200:
            pass

    @classmethod
    def _get(cls, url: str, headers: Dict[str, str], json: Dict[str, str], params: Dict[str, str], **kwargs):

        response = requests.get(
            url=url,
            headers=headers,
            json=json,
            params=params
        )




