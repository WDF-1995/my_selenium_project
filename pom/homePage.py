# -*- coding:utf-8 -*-
"""
@Auth：Richard
@Time：2022年01月06日
"""
import time

from pom.basePage import BasePage


class HomePage(BasePage):
    def __init__(self, login):
        BasePage.__init__(self, login.driver)
        self.user_btn = ('xpath', '//*[@id="app"]/div/div[2]/div/div[1]/div[3]/div/div/i')  # 用户头像
        self.logout_btn = ('css selector', '.el-popper > span:nth-child(3) > li')  # 退出登录按钮
        self.confirm_btn = ('class name', 'el-button--primary')  # 确认退出登录按钮
        self.sys_manage_btn = ('xpath', '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/li/div/i')  # 系统管理
        self.sys_user_manage_btn = ('xpath', '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/li/ul/a[1]/li')  # 用户管理

    def enter_user_manage(self):
        self.click(*self.sys_manage_btn)
        self.logger.info('点击系统管理')
        time.sleep(0.5)
        self.click(*self.sys_user_manage_btn)
        self.logger.info('点击用户管理')

    def logout(self):
        self.click(*self.user_btn)
        self.logger.info('点击头像')
        time.sleep(0.5)
        self.click(*self.logout_btn)
        self.logger.info('点击logout')
        self.click(*self.confirm_btn)
        self.logger.info('点击确认退出按钮')

