# Web UI自动化测试框架

基于pytest + selenium的Web UI自动化测试框架,使用Page Object模式设计。

## 项目结构

```
├── config/             # 配置文件目录
├── page_objects/       # 页面对象目录
│   ├── base_page.py   # 基础页面类
│   └── baidu_page.py  # 百度页面类
├── test_cases/        # 测试用例目录
│   └── test_baidu.py  # 测试用例
├── reports/           # 测试报告目录
├── utils/             # 工具类目录
├── conftest.py        # pytest配置文件
└── requirements.txt   # 项目依赖
```

## 环境要求

- Python 3.7+
- Chrome浏览器

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行测试

```bash
pytest testcase/ --html=reports/report.html
```

## 主要特性

- 使用Page Object模式封装页面元素
- 支持HTML测试报告
- 自动管理WebDriver
- 支持显式等待
- 可扩展的框架结构 