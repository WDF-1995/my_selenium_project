# -*- coding:utf-8 -*-
"""
@Auth：Richard
@Time：2021年12月11日
"""
import os
import time
import unittest
# from lib.baidu_api import read_picture
from selenium import webdriver
from pom.adminLoginPage import AdminLoginPage
from ddt import ddt, data, unpack, file_data

path = os.path.dirname(os.path.dirname(__file__)) + '/data'


@ddt
class TestAdminLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.loginPage = AdminLoginPage(cls.driver)
        cls.logger = cls.loginPage.logger
        cls.logger.info('**********打开浏览器，开始测试**********')
        cls.loginPage.goto_login_page()

    @classmethod
    def tearDownClass(cls) -> None:
        # pass
        cls.loginPage.quit_browser()
        cls.logger.info('**********关闭浏览器，结束测试**********\n\n')
        time.sleep(3)
        # cls.logger.info('----强制等待3s----\n\n')

    def setUp(self) -> None:
        self.loginPage.refresh_browser()
        self.logger.info('刷新页面')

    def tearDown(self) -> None:
        pass
        # time.sleep(3)
        # self.logger.info('----强制等待3s----')

    @file_data(path + '/login_fail.yaml')
    def test1_login_failed(self, **login):
        """测试登录失败"""
        self.logger.info('\n\n--------------执行测试: %s ---------------', login.get('case'))
        self.loginPage.admin_login_error(login.get('username'), login.get('password'), login.get('captcha'))
        self.logger.info('开始断言')
        if login.get('case') == '测试输入错误验证码登录失败':
            # 判断验证码错误提示框
            print(login.get('case'))
            try:
                result = self.loginPage.find_element('xpath', '/html/body/div[last()]/div[1]/h2')
                self.assertEqual(result.text, login.get('expected'))
                self.logger.info('测试通过')
            except Exception as e:
                self.logger.error('测试未通过 %s', e, exc_info=1)
                raise e

        elif login.get('case') == '测试输入验证码为空登录失败':
            # 判断输入验证码为空提示
            print(login.get('case'))
            try:
                time.sleep(0.5)  # 需强制等待，否则元素存在但定位不到文本
                result = self.loginPage.find_element('xpath', '//*[@id="app"]/div/form/div[3]/div/div[3]')
                self.assertEqual(result.text, login.get('expected'))
                self.logger.info('测试通过')
            except Exception as e:
                self.logger.error('测试未通过 %s', e, exc_info=1)
                raise e

        elif login.get('case') == '测试输入用户名为空登录失败':
            # 判断输入用户名为空提示
            print(login.get('case'))
            try:
                result = self.loginPage.find_element('xpath',
                                                     '//*[@id="app"]/div/form/div[1]/div/div[2]')
                self.assertEqual(result.text, login.get('expected'))
                self.logger.info('测试通过')
            except Exception as e:
                self.logger.error('测试未通过 %s', e, exc_info=1)
                raise e

        elif login.get('case') == '测试输入密码为空登录失败':
            # 判断输入密码为空提示
            print(login.get('case'))
            try:
                result = self.loginPage.find_element('xpath',
                                                     '//*[@id="app"]/div/form/div[2]/div/div[2]')
                self.assertEqual(result.text, login.get('expected'))
                self.logger.info('测试通过')
            except Exception as e:
                self.logger.error('测试未通过 %s', e, exc_info=1)
                raise e
        else:
            print('测试数据有误，请检查')
        self.logger.info('\n--------------执行完毕: %s ---------------\n', login.get('case'))

    @file_data(path + '/login_success.yaml')
    def test2_login_success(self, **login):
        """测试登录成功"""
        self.logger.info('\n--------------执行测试: %s ---------------', login.get('case'))
        self.loginPage.admin_login_success(login.get('username'), login.get('password'), login.get('captcha'))
        print(login.get('case'))
        self.logger.info('开始断言')
        try:
            result = self.loginPage.find_element('xpath',
                                                 '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/span/span/span[1]/span')
            self.assertEqual(result.text, login.get('expected'))
            self.logger.info('测试通过')
        except Exception as e:
            self.logger.error("测试未通过 %s", e, exc_info=1)
            raise e
        self.logger.info('\n--------------执行完毕: %s ---------------\n', login.get('case'))
