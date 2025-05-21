from selenium.webdriver.common.by import By

from config.setting import WEBURL
from .base_page import BasePage

class BaiduPage(BasePage):
    # 页面元素定位器
    
    # 搜索输入框
    search_input = (By.ID, "kw")
    # 搜索按钮
    search_button = (By.ID, "su")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = WEBURL
    
    def open(self):
        """打开百度首页"""
        self.driver.get(self.url)
    
    def search(self, keyword):
        """搜索关键词"""
        self.input_text(self.search_input, keyword)
        self.click(self.search_button) 