import time

import pytest
import logging

from conftest import driver
from page_objects.simple_page import SimplePage

log = logging.getLogger('Test_Helloworld')

class TestSimpleAI:

    @pytest.mark.parametrize("username, password, expected",[("szwnba", "982128", "欢迎") ])
    def test_login(self, driver,  username, password, expected):
        simple_page = SimplePage(driver)
        simple_page.login(username, password)
        assert driver.title == 'Simple AI Platform'

