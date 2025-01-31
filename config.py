import os
import yaml

def get_project_root():
    # 获取当前文件的绝对路径
    current_file_path = os.path.abspath(__file__)
    # 获取当前文件所在的目录
    root_dir = os.path.dirname(current_file_path)
    return root_dir

class Config:
    def __init__(self, config_file='config.yaml'):
        # 获取项目的根目录
        root_dir = get_project_root()
        config_path = os.path.join(root_dir, config_file)

        # 确保路径正确
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found at {config_path}")

        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        self.environment = self.config['default_environment']

    def get_transaction_domain(self):
        return self.config['environments'][self.environment]['transaction_domain']

    def get_social_domain(self):
        return self.config['environments'][self.environment]['social_domain']

