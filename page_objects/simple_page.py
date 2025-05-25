from selenium.webdriver.common.by import By
import time
from config.setting import WEBURL
from conftest import driver
from .base_page import BasePage

class SimplePage(BasePage):
    # 页面元素定位器
    name_input = (By.NAME, "username")

    # 页面元素定位器
    pwd_input = (By.NAME, "password")

    # 搜索按钮
    login_button = (By.CSS_SELECTOR, ".el-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://43.139.136.165:8000/"
    
    def open(self):
        """打开百度首页"""
        self.driver.get(self.url)
    
    def login(self, username,password):
        """搜索关键词"""
        self.open()
        self.input_text(self.name_input, username)
        self.input_text(self.pwd_input, password)
        self.click(self.login_button)
        time.sleep(2)