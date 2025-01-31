project/
├── src/                     # 源代码目录
│   ├── __init__.py          # 确保 src 是一个 Python 包
│   ├── transaction/         # 业务模块
│   │   ├── __init__.py      # 确保 transaction 是一个 Python 包
│   │   ├── module1.py       # 模块1的实现
│   │   └── module2.py       # 模块2的实现
│   └── social/              # 业务模块
│       ├── __init__.py      # 确保 social 是一个 Python 包
│       ├── module1.py       # 模块1的实现
│       └── module2.py       # 模块2的实现
├── tests/                   # 测试代码目录
│   ├── __init__.py          # 确保 tests 是一个 Python 包
│   ├── conftest.py          # 共享的测试配置
│   ├── test_transaction/    # 测试 transaction 模块
│   │   ├── __init__.py      # 确保 test_transaction 是一个 Python 包
│   │   ├── test_module1.py  # 测试 module1
│   │   └── test_module2.py  # 测试 module2
│   └── test_social/         # 测试 social 模块
│       ├── __init__.py      # 确保 test_social 是一个 Python 包
│       ├── test_module1.py  # 测试 module1
│       └── test_module2.py  # 测试 module2
├── config/                  # 配置文件目录
│   ├── __init__.py          # 确保 config 是一个 Python 包
│   ├── config.yaml          # 配置文件
│   └── config.py            # 配置读取和管理逻辑
├── .github/                 # GitHub Actions 或其他 CI/CD 配置
│   └── workflows/
│       └── ci.yml           # 示例 CI 工作流
├── .gitignore               # 忽略文件配置
├── pytest.ini               # pytest 配置文件
├── README.md                # 项目说明文档
└── setup.py                 # 项目打包和发布配置（如果需要）
