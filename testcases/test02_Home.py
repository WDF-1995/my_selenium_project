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

    def test01_enter_user_manage(self, **home):
        self.logger.info('\n\n--------------执行测试: %s ---------------', '测试进入用户管理')
        self.login.goto_login_page()
        self.login.admin_login_success('test', '123456')
        self.home.enter_sys_manage()
        time.sleep(0.5)
        self.home.enter_user_manage()
        self.logger.info('开始断言')
        print('测试进入用户管理')
        try:
            result = self.home.find_element('xpath',
                                            '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[2]/div[2]/table/thead/tr/th[1]/div')
            self.assertIsNotNone(result)
            self.logger.info('测试通过')
        except Exception as e:
            self.logger.error('测试未通过 %s', e, exc_info=1)
            raise e
        self.logger.info('\n--------------执行完毕: %s ---------------\n', '测试进入用户管理')

    def test02_enter_role_manage(self, **home):
        self.logger.info('\n\n--------------执行测试: %s ---------------', '测试进入角色管理')
        self.home.enter_role_manage()
        self.logger.info('开始断言')
        print('测试进入角色管理')
        try:
            result = self.home.find_element('xpath',
                                            '//*[@id="app"]/div/div[2]/section/div/div[3]/div[1]/div/div[1]/div/span')
            self.assertEqual(result.text, '角色列表')
            self.logger.info('测试通过')
        except Exception as e:
            self.logger.error('测试未通过 %s', e, exc_info=1)
            raise e
        self.logger.info('\n--------------执行完毕: %s ---------------\n', '测试进入角色管理')

    def test03_enter_menu_manage(self, **home):
        self.logger.info('\n\n--------------执行测试: %s ---------------', '测试进入菜单管理')
        self.home.enter_menu_manage()
        self.logger.info('开始断言')
        print('测试进入菜单管理')
        try:
            result = self.home.find_element('xpath',
                                            '//*[@id="app"]/div/div[2]/section/div/div[3]/div[2]/table/thead/tr/th[1]/div')
            self.assertEqual(result.text, '菜单名称')
            self.logger.info('测试通过')
        except Exception as e:
            self.logger.error('测试未通过 %s', e, exc_info=1)
            raise e
        self.logger.info('\n--------------执行完毕: %s ---------------\n', '测试进入菜单管理')

    def test04_enter_department_manage(self, **home):
        self.logger.info('\n\n--------------执行测试: %s ---------------', '测试进入部门管理')
        self.home.enter_department_manage()
        self.logger.info('开始断言')
        print('测试进入部门管理')
        try:
            result = self.home.find_element('xpath',
                                            '//*[@id="app"]/div/div[2]/section/div/div[1]/div[3]/div[1]/input')
            self.assertIsNotNone(result)
            self.logger.info('测试通过')
        except Exception as e:
            self.logger.error('测试未通过 %s', e, exc_info=1)
            raise e
        self.logger.info('\n--------------执行完毕: %s ---------------\n', '测试进入部门管理')

    def test05_enter_post_manage(self, **home):
        self.logger.info('\n\n--------------执行测试: %s ---------------', '测试进入岗位管理')
        self.home.enter_post_manage()
        self.logger.info('开始断言')
        print('测试进入岗位管理')
        try:
            result = self.home.find_element('xpath',
                                            '//*[@id="app"]/div/div[2]/section/div/div[3]/div[4]/div[1]/table/thead/tr/th[6]/div')
            self.assertIsNotNone(result)
            self.logger.info('测试通过')
        except Exception as e:
            self.logger.error('测试未通过 %s', e, exc_info=1)
            raise e
        self.logger.info('\n--------------执行完毕: %s ---------------\n', '测试进入岗位管理')

    def test06_enter_dict_manage(self, **home):
        self.logger.info('\n\n--------------执行测试: %s ---------------', '测试进入字典管理')
        self.home.enter_dict_manage()
        self.logger.info('开始断言')
        print('测试进入字典管理')
        try:
            result = self.home.find_element('xpath',
                                            '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div/div[1]/div/span')
            self.assertEqual(result.text, '字典详情')
            self.logger.info('测试通过')
        except Exception as e:
            self.logger.error('测试未通过 %s', e, exc_info=1)
            raise e
        self.logger.info('\n--------------执行完毕: %s ---------------\n', '测试进入字典管理')

    def test07_logout(self, **logout):
        self.logger.info('\n\n--------------执行测试: %s ---------------', '测试退出登录成功')
        self.home.logout()
        self.logger.info('开始断言')
        print('测试退出登录成功')
        try:
            result = self.home.find_element('xpath', '//*[@id="app"]/div/form/h3')
            self.assertEqual(result.text, 'ICoin Management System')
            self.logger.info('测试通过')
        except Exception as e:
            self.logger.error('测试未通过 %s', e, exc_info=1)
            raise e
        self.logger.info('\n--------------执行完毕: %s ---------------\n', '测试退出登录成功')


if __name__ == '__main__':
    unittest.main()
