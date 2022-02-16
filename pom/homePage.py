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
        self.user_btn = ('xpath', '//*[@id="app"]/div/div[2]/div/div[1]/div[3]/div/div/i')
        self.logout_btn = ('css selector', '.el-popper > span:nth-child(3) > li')
        self.confirm_btn = ('class name', 'el-button--primary')

    def logout(self):
        self.click(*self.user_btn)
        self.logger.info('点击头像')
        time.sleep(0.5)
        self.click(*self.logout_btn)
        self.logger.info('点击logout')
        self.click(*self.confirm_btn)
        self.logger.info('点击确认退出按钮')

