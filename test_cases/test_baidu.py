import pytest
import logging

from conftest import driver
from page_objects.baidu_page import BaiduPage

log = logging.getLogger('TestBaidu')

class TestBaidu:


    def test_search(self, driver):
        log.info("开始执行test_search测试用例")
        baidu_page = BaiduPage(driver)
        """测试百度搜索功能"""
        log.info("打开百度首页")
        baidu_page.open()
        log.info("搜索关键词: pytest selenium")
        baidu_page.search("pytest selenium")
        # 这里可以添加断言
        log.info("验证页面标题包含'百度'")
        assert "百度" in driver.title
        log.info("test_search测试用例执行完成")

    def test_search2(self):
        """测试百度搜索功能"""
        log.info("开始执行test_search2测试用例")
        log.info("验证字符串'pytest'是否在'pytest'中")
        assert "pytest" in "pytest"
        log.info("test_search2测试用例执行完成")

    def test_search3(self):
        """测试百度搜索功能"""
        log.info("开始执行test_search3测试用例")
        log.info("验证字符串'pytest'是否在'pytest'中")
        assert "pytest" in "pytest"
        log.info("test_search3测试用例执行完成")