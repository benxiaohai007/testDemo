import pytest
import requests
from config import Config

@pytest.fixture(scope="module")
def config():
    return Config()

class TestTransactionEndpoints:
    def __init__(self, config):
        self.transaction_domain = config.get_transaction_domain()

    def test_get_transaction_endpoint(self):
        response = requests.get(f"{self.transaction_domain}/api/endpoint1")
        assert response.status_code == 200


    def test_post_transaction_endpoint(self):
        data = {"key": "value"}
        response = requests.post(f"{self.transaction_domain}/api/endpoint2", json=data)
        assert response.status_code == 200

    # 添加更多测试用例
    def test_another_transaction_request(self):
        response = requests.get(f"{self.transaction_domain}/api/another-endpoint")
        assert response.status_code == 200

    # 继续添加更多测试用例...
