import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os
import logging

from config.setting import TEST_REPORT

@pytest.fixture(scope="session")
# 定义了一个会话级的测试夹具（fixture），名为 driver。它的功能是：
# 在整个测试会话中只执行一次该 fixture
# 通常用于初始化和共享资源，如浏览器驱动
# 被标记为 fixture 的函数可以被多个测试用例复用
def driver():
    try:
        # 配置Chrome选项
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--ignore-certificate-errors')
        # chrome_options.add_argument('--headless=new')
        chrome_options.add_experimental_option('useAutomationExtension', False)
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

# 配置日志路径
def pytest_configure(config):
    # 配置测试报告
    config.option.htmlpath = f"{TEST_REPORT}/report.html"