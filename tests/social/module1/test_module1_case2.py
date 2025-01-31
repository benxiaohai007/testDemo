import pytest
import requests
from config import Config

config = Config()

@pytest.fixture(scope="module")
def social_domain():
    return config.get_social_domain()

def test_get_request(social_domain):
    response = requests.get(f"{social_domain}/api/endpoint3")
    assert response.status_code == 200

def test_post_request(social_domain):
    data = {"key": "value"}
    response = requests.post(f"{social_domain}/api/endpoint4", json=data)
    assert response.status_code == 201
