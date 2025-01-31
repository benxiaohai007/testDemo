import pytest
import yaml
import os
from unittest.mock import mock_open

# 假设 Config 类在 config.py 文件中
from config import Config

def test_config_file_exists_and_valid(monkeypatch):
    config_data = yaml.dump({
        'default_environment': 'test',
        'environments': {
            'test': {
                'transaction_domain': 'https://test-transaction.example.com',
                'social_domain': 'https://test-social.example.com'
            },
            'staging': {
                'transaction_domain': 'https://staging-transaction.example.com',
                'social_domain': 'https://staging-social.example.com'
            },
            'production': {
                'transaction_domain': 'https://transaction.example.com',
                'social_domain': 'https://social.example.com'
            }
        }
    })
    mock_file = mock_open(read_data=config_data)

    # 模拟 os.path.exists 返回 True
    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    # 模拟 builtins.open 返回 mock_file
    monkeypatch.setattr('builtins.open', mock_file)
    # 模拟 get_project_root 返回模拟的根目录
    mock_root_dir = '/mocked/root/directory'
    monkeypatch.setattr('config.get_project_root', lambda: mock_root_dir)

    config = Config()
    assert config.get_transaction_domain() == 'https://test-transaction.example.com'
    assert config.get_social_domain() == 'https://test-social.example.com'

def test_config_file_does_not_exist(monkeypatch):
    # 模拟 os.path.exists 返回 False
    monkeypatch.setattr(os.path, 'exists', lambda x: False)
    # 模拟 get_project_root 返回模拟的根目录
    mock_root_dir = '/mocked/root/directory'
    monkeypatch.setattr('config.get_project_root', lambda: mock_root_dir)

    with pytest.raises(FileNotFoundError):
        Config()

def test_config_environment_does_not_exist(monkeypatch):
    config_data = yaml.dump({
        'default_environment': 'nonexistent',
        'environments': {
            'test': {
                'transaction_domain': 'https://test-transaction.example.com',
                'social_domain': 'https://test-social.example.com'
            },
            'staging': {
                'transaction_domain': 'https://staging-transaction.example.com',
                'social_domain': 'https://staging-social.example.com'
            },
            'production': {
                'transaction_domain': 'https://transaction.example.com',
                'social_domain': 'https://social.example.com'
            }
        }
    })
    mock_file = mock_open(read_data=config_data)

    # 模拟 os.path.exists 返回 True
    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    # 模拟 builtins.open 返回 mock_file
    monkeypatch.setattr('builtins.open', mock_file)
    # 模拟 get_project_root 返回模拟的根目录
    mock_root_dir = '/mocked/root/directory'
    monkeypatch.setattr('config.get_project_root', lambda: mock_root_dir)

    with pytest.raises(KeyError):
        config = Config()
        config.get_transaction_domain()

def test_config_domain_does_not_exist(monkeypatch):
    config_data = yaml.dump({
        'default_environment': 'test',
        'environments': {
            'test': {
                'transaction_domain': 'https://test-transaction.example.com'
            },
            'staging': {
                'transaction_domain': 'https://staging-transaction.example.com',
                'social_domain': 'https://staging-social.example.com'
            },
            'production': {
                'transaction_domain': 'https://transaction.example.com',
                'social_domain': 'https://social.example.com'
            }
        }
    })
    mock_file = mock_open(read_data=config_data)

    # 模拟 os.path.exists 返回 True
    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    # 模拟 builtins.open 返回 mock_file
    monkeypatch.setattr('builtins.open', mock_file)
    # 模拟 get_project_root 返回模拟的根目录
    mock_root_dir = '/mocked/root/directory'
    monkeypatch.setattr('config.get_project_root', lambda: mock_root_dir)

    with pytest.raises(KeyError):
        config = Config()
        config.get_social_domain()
