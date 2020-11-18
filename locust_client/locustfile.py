import time
from locust import HttpUser, task, between


class QuickStartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def index_page(self):
        pass

    @task(3)
    def view_item(self):
        pass

    @task
    def share_tag(self):
        data = {
            "external_id": 1,
            "external_type": 2,
            "page": 1,
            "tenant_code": "htportal",
            "share_user": 1,
            "source": "crm_applet",
        }
        self.client.post('/api/v1/share/tag/generate/', json=data)

