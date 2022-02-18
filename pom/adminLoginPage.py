# -*- coding:utf-8 -*-
"""
@Auth：Richard
@Time：2021年12月11日
"""
import os
import time

# from lib.baidu_api import read_picture
from pom.basePage import BasePage
from util.util import get_code


class AdminLoginPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.username_input = ('xpath', '//*[@id="app"]/div/form/div[1]/div/div[1]/input')
        self.pwd_input = ('xpath', '//*[@id="app"]/div/form/div[2]/div/div[1]/input')
        self.captcha_input = ('xpath', '//*[@id="app"]/div/form/div[3]/div/div[1]/input')
        self.agree_btn = ('xpath', '//*[@id="app"]/div/form/label/span[1]/span')
        self.login_btn = ('xpath', '//*[@id="app"]/div/form/div[4]/div/button')
        self.code_pic = ('xpath', '//*[@id="app"]/div/form/div[3]/div/div[2]/img')

    def goto_login_page(self):
        self.driver.get('http://120.25.153.60:84/login')
        self.driver.maximize_window()
        self.logger.info('进入登录页面')

    def click_remember_btn(self):
        self.click(*self.agree_btn)


    def admin_login_error(self, username, password, captcha):
        self.type_text(username, *self.username_input)
        self.logger.info('输入用户名 %s', username)
        self.type_text(password, *self.pwd_input)
        self.logger.info('输入密码 %s', password)
        self.type_text(captcha, *self.captcha_input)
        self.logger.info('输入验证码 %s ', captcha)
        self.click(*self.login_btn)
        self.logger.info('点击登录按钮')

    def admin_login_success(self, username, password, captcha=None):
        self.type_text(username, *self.username_input)
        self.logger.info('输入用户名 %s', username)
        self.type_text(password, *self.pwd_input)
        self.logger.info('输入密码 %s', password)
        self.type_text(get_code(), *self.captcha_input)
        self.logger.info('输入验证码 %s ', get_code())
        self.click(*self.login_btn)
        self.logger.info('点击登录按钮')

    # def get_code_picture(self):
    #     """保存验证码图片"""
    #     picture_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
    #     path = os.path.dirname(os.path.dirname(__file__)) + '\\screenshots'
    #     picture_name = path + '\\' + str(picture_time) + '.png'
    #     self.find_element(*self.code_pic).screenshot(picture_name)
    #     return picture_name

        # # 识别验证码
        # code_pic = self.get_code_picture()
        # captcha = read_picture(code_pic)
        # self.logger.info('第三方验证码识别结果为 %s', captcha)
        # self.type_text(captcha, *self.captcha_input)
        # self.logger.info('输入验证码 %s', captcha)
        # self.click(*self.login_btn)
