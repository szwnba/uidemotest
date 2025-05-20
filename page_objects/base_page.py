from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging
import time
import os
from datetime import datetime


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(self.__class__.__name__)

    def find_element(self, locator):
        """查找单个元素"""
        self.logger.info(f"查找元素: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """查找多个元素"""
        self.logger.info(f"查找多个元素: {locator}")
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        """点击元素"""
        self.logger.info(f"点击元素: {locator}")
        element = self.find_element(locator)
        element.click()

    def input_text(self, locator, text):
        """输入文本"""
        self.logger.info(f"在元素 {locator} 中输入文本: {text}")
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """获取元素文本"""
        self.logger.info(f"获取元素 {locator} 的文本")
        element = self.find_element(locator)
        return element.text

    # 等待相关方法
    def wait_for_element_visible(self, locator, timeout=10):
        """等待元素可见"""
        self.logger.info(f"等待元素可见: {locator}, 超时时间: {timeout}秒")
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator, timeout=10):
        """等待元素可点击"""
        self.logger.info(f"等待元素可点击: {locator}, 超时时间: {timeout}秒")
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_element_disappear(self, locator, timeout=10):
        """等待元素消失"""
        self.logger.info(f"等待元素消失: {locator}, 超时时间: {timeout}秒")
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    # 元素状态判断方法
    def is_element_present(self, locator):
        """判断元素是否存在"""
        try:
            self.find_element(locator)
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def is_element_visible(self, locator):
        """判断元素是否可见"""
        try:
            return self.wait_for_element_visible(locator)
        except (TimeoutException, NoSuchElementException):
            return False

    def is_element_enabled(self, locator):
        """判断元素是否可用"""
        try:
            element = self.find_element(locator)
            return element.is_enabled()
        except (TimeoutException, NoSuchElementException):
            return False

    # 鼠标操作相关方法
    def hover(self, locator):
        """鼠标悬停"""
        self.logger.info(f"鼠标悬停在元素上: {locator}")
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self, locator):
        """双击元素"""
        self.logger.info(f"双击元素: {locator}")
        element = self.find_element(locator)
        ActionChains(self.driver).double_click(element).perform()

    def right_click(self, locator):
        """右键点击元素"""
        self.logger.info(f"右键点击元素: {locator}")
        element = self.find_element(locator)
        ActionChains(self.driver).context_click(element).perform()

    def drag_and_drop(self, source_locator, target_locator):
        """拖拽元素"""
        self.logger.info(f"拖拽元素从 {source_locator} 到 {target_locator}")
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    # 键盘操作相关方法
    def press_enter(self, locator):
        """按回车键"""
        self.logger.info(f"在元素 {locator} 上按回车键")
        element = self.find_element(locator)
        element.send_keys(Keys.ENTER)

    def press_escape(self, locator):
        """按ESC键"""
        self.logger.info(f"在元素 {locator} 上按ESC键")
        element = self.find_element(locator)
        element.send_keys(Keys.ESCAPE)

    def press_tab(self, locator):
        """按Tab键"""
        self.logger.info(f"在元素 {locator} 上按Tab键")
        element = self.find_element(locator)
        element.send_keys(Keys.TAB)

    # 页面操作相关方法
    def refresh(self):
        """刷新页面"""
        self.logger.info("刷新页面")
        self.driver.refresh()

    def back(self):
        """返回上一页"""
        self.logger.info("返回上一页")
        self.driver.back()

    def forward(self):
        """前进到下一页"""
        self.logger.info("前进到下一页")
        self.driver.forward()

    def get_current_url(self):
        """获取当前URL"""
        self.logger.info("获取当前URL")
        return self.driver.current_url

    def get_page_title(self):
        """获取页面标题"""
        self.logger.info("获取页面标题")
        return self.driver.title

    def get_page_source(self):
        """获取页面源码"""
        self.logger.info("获取页面源码")
        return self.driver.page_source

    # 截图相关方法
    def take_screenshot(self, name=None):
        """截图"""
        if name is None:
            name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # 确保screenshots目录存在
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')
            
        file_path = os.path.join('screenshots', f"{name}.png")
        self.logger.info(f"截图保存到: {file_path}")
        self.driver.save_screenshot(file_path)
        return file_path

    def take_element_screenshot(self, locator, name=None):
        """对元素进行截图"""
        if name is None:
            name = f"element_screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
        element = self.find_element(locator)
        self.logger.info(f"对元素 {locator} 进行截图")
        
        # 确保screenshots目录存在
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')
            
        file_path = os.path.join('screenshots', f"{name}.png")
        element.screenshot(file_path)
        return file_path

    # JavaScript相关方法
    def execute_script(self, script, *args):
        """执行JavaScript脚本"""
        self.logger.info(f"执行JavaScript脚本: {script}")
        return self.driver.execute_script(script, *args)

    def scroll_to_element(self, locator):
        """滚动到元素位置"""
        self.logger.info(f"滚动到元素位置: {locator}")
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to_bottom(self):
        """滚动到页面底部"""
        self.logger.info("滚动到页面底部")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        """滚动到页面顶部"""
        self.logger.info("滚动到页面顶部")
        self.driver.execute_script("window.scrollTo(0, 0);") 