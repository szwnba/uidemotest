import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os
import logging

# 配置日志
def setup_logging():
    # 创建logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # 创建文件处理器
    # 确保reports目录存在
    if not os.path.exists('logs'):
        os.makedirs('logs')
    log_file = f"logs/test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    
    # 创建格式化器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    # 添加处理器到logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

@pytest.fixture(scope="session", autouse=True)
def logger():
    return setup_logging()

@pytest.fixture(scope="session")
# 定义了一个会话级的测试夹具（fixture），名为 driver。它的功能是：
# 在整个测试会话中只执行一次该 fixture
# 通常用于初始化和共享资源，如浏览器驱动、数据库连接等
# 被标记为 fixture 的函数可以被多个测试用例复用
def driver():
    try:
        # 配置Chrome选项
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--ignore-certificate-errors')
        
        # 初始化Chrome浏览器
        driver_path = os.path.join(os.path.dirname(__file__), ".", "driver", "chromedriver.exe")
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.maximize_window()
        yield driver
    except Exception as e:
        print(f"启动Chrome浏览器失败: {str(e)}")
        raise
    finally:
        if 'driver' in locals():
            driver.quit()


def pytest_configure(config):
    # 确保reports目录存在
    if not os.path.exists('reports'):
        os.makedirs('reports')
    # 配置测试报告
    config.option.htmlpath = f"reports/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"