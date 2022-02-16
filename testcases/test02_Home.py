# -*- coding:utf-8 -*-
"""
@Auth：Richard
@Time：2022年01月06日
"""
import os
import time
import unittest

from ddt import ddt, data, unpack, file_data
from selenium import webdriver

from pom.adminLoginPage import AdminLoginPage
from pom.homePage import HomePage

path = os.path.dirname(os.path.dirname(__file__)) + '/data'


@ddt
class TestHome(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.login = AdminLoginPage(cls.driver)
        cls.home = HomePage(cls.login)
        cls.logger = cls.home.logger
        cls.logger.info('**********打开浏览器，开始测试**********')

    @classmethod
    def tearDownClass(cls) -> None:
        # pass
        cls.home.quit_browser()
        cls.logger.info('**********关闭浏览器，结束测试**********\n\n')
        time.sleep(3)
        cls.logger.info('----强制等待3s----\n\n')

    def setUp(self) -> None:
        pass
        # self.loginPage.refresh_browser()
        # self.logger.info('*刷新页面*')

    def tearDown(self) -> None:
        pass
        # time.sleep(2)
        # self.logger.info('----强制等待2s----')

    @file_data(path + '/logout_success.yaml')
    def test01_logout(self, **logout):
        self.logger.info('\n\n--------------执行测试: %s ---------------', logout.get('case'))
        self.login.goto_login_page()
        self.logger.info('进入登录页面')
        self.login.admin_login_success(logout.get('username'), logout.get('password'))
        self.home.logout()
        self.logger.info('开始断言')
        print(logout.get('case'))
        try:
            result = self.home.find_element('xpath', '//*[@id="app"]/div/form/h3')
            self.assertEqual(result.text, logout.get('expected'))
            self.logger.info('测试通过')
        except Exception as e:
            self.logger.error('测试未通过 %s', e, exc_info=1)
            raise e
        self.logger.info('\n--------------执行完毕: %s ---------------\n', logout.get('case'))


# if __name__ == '__main__':
#     unittest.main()
