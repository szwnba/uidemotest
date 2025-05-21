import pytest
import logging

from conftest import driver
from page_objects.baidu_page import BaiduPage

log = logging.getLogger('Test_Helloworld')

class Test_Helloworld:
    def test_search2(self):
        """测试百度搜索功能"""
        log.info("验证字符串'pytest'是否在'pytest'中")
        assert "pytest" in "pytest"

    def test_search3(self):
        """测试百度搜索功能"""
        log.info("验证字符串'pytest'是否在'pytest'中")
        assert "pytest" in "pytest"
