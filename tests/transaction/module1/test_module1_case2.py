import pytest
import requests
from config import Config

config = Config()

@pytest.fixture(scope="module")
def transaction_domain():
    return config.get_transaction_domain()

def test_get_request(transaction_domain):
    response = requests.get(f"{transaction_domain}/api/endpoint3")
    assert response.status_code == 200

def test_post_request(transaction_domain):
    data = {"key": "value"}
    response = requests.post(f"{transaction_domain}/api/endpoint4", json=data)
    assert response.status_code == 201
