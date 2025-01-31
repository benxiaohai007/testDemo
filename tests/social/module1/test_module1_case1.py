import pytest
import requests
from config import Config

@pytest.fixture(scope="module")
def config():
    return Config()

class TestSocialEndpoints:
    def __init__(self, config):
        self.social_domain = config.get_social_domain()

    def test_get_request(self):
        response = requests.get(f"{self.social_domain}/api/endpoint1")
        assert response.status_code == 200

    def test_post_request(self):
        data = {"key": "value"}
        response = requests.post(f"{self.social_domain}/api/endpoint2", json=data)
        assert response.status_code == 201

    # 添加更多测试用例
    def test_another_request(self):
        response = requests.get(f"{self.social_domain}/api/another-endpoint")
        assert response.status_code == 200

    # 继续添加更多测试用例...
