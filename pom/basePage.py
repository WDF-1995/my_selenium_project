# -*- coding:utf-8 -*-
"""
@Auth：Richard
@Time：2021年12月11日
"""
from selenium.webdriver.support.wait import WebDriverWait

from util.util import get_logger


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger()

    def find_element(self, *loc, timeout=15):
        """
            方法：动态查找元素，显式等待
            参数：
                locator：元素定位的方式和值
                    - ('id', 'kw')                      # driver.find_element_by_id('kw')
                    - ('xpath', 'xxxxx')
                    - ('name', 'xxx')
                    - ('css selector', 'xxxx')
                    - ('class name', 'xxxx')            # driver.find_element_by_class_name
                    - ('link text', 'xxxx')             # driver.find_element_by_link_text
                    - ('partial link text', 'xxx')      # driver.find_element_by_partial_link_text
                timeout：找元素的超时时间，默认15
            返回值：
                找到元素就返回元素，没有做找到元素就报错，timeout
        """
        try:
            return WebDriverWait(self.driver, timeout).until(lambda s: s.find_element(*loc))
        except Exception as e:
            self.logger.error('元素定位失败: %s ', e)

    def type_text(self, text, *loc):
        self.find_element(*loc).send_keys(text)

    def click(self, *loc):
        self.find_element(*loc).click()

    def clear(self, *loc):
        self.find_element(*loc).clear()

    def get_title(self):
        return self.driver.title

    def quit_browser(self):
        self.driver.quit()

    def refresh_browser(self):
        self.driver.refresh()
