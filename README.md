project/
├── tests/
│   ├── transaction/
│   │   ├── module1/
│   │   │   ├── test_module1_case1.py
│   │   │   └── test_module1_case2.py
│   │   └── module2/
│   │       ├── test_module2_case1.py
│   │       └── test_module2_case2.py
│   └── social/
│       ├── module1/
│       │   ├── test_module1_case1.py
│       │   └── test_module1_case2.py
│       └── module2/
│           ├── test_module2_case1.py
│           └── test_module2_case2.py
├── config.yaml
├── pytest.ini
└── README.md
## 配置文件
- `config.yaml`: 配置不同环境的域名和默认环境

## pytest配置文件
- `pytest.ini`: 配置pytest的运行参数

## 测试用例
- `tests/transaction/module1/test_module1_case1.py`: 示例测试用例文件
- `tests/transaction/module1/test_module1_case2.py`: 示例测试用例文件
- `tests/social/module1/test_module1_case1.py`: 示例测试用例文件
- `tests/social/module1/test_module1_case2.py`: 示例测试用例文件

## 配置类
- `config.py`: 读取配置文件并提供获取域名的方法
