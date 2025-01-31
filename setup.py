# setup.py
from setuptools import setup, find_packages

setup(
    name='testDemo',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # 添加项目依赖
    ],
    entry_points={
        'console_scripts': [
            # 添加命令行入口点
        ],
    },
)
