# -*- coding:utf-8 -*-
"""
@Auth：Richard
@Time：2021年12月07日
"""
import configparser
import os
import re
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from lib.HTMLTestRunner import HTMLTestRunner

from util.util import send_mail, get_logger, get_code

if __name__ == '__main__':
    testcase = unittest.defaultTestLoader.discover('testcases', 'test*.py')
    filepath = 'reports/Test.html'
    title = 'Moneyloanplus催收后台自动测试报告'
    descr = '自动测试'
    tester = 'Richard'
    with open(file=filepath, mode='wb') as report:
        runner = HTMLTestRunner(stream=report, title=title, description=descr, tester=tester)
        runner.run(testcase)
    send_mail(filepath)
    get_logger().info('send_email success')
    #
    # driver = webdriver.Chrome()
    # driver.get('http://120.25.153.60:84/login')
    # driver.find_element_by_xpath('//*[@id="app"]/div/form/div[1]/div/div[1]/input').send_keys('test')
    # driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div/div/input').send_keys('123456')
    #
    # time.sleep(20)
    # e= driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div[1]/div/div[1]/div/span')
    # print(e.text)
    # print(e)


    # path = os.path.dirname(__file__) + '\config'
    # configPath = os.path.join(path, "config.ini")
    #
    # conf = configparser.ConfigParser()
    # conf.read(configPath)
    # secs = conf.sections()  # 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，
    #
    # print(secs)
    #
    # options = conf.options("Mysql-Database")  # 获取某个section名为Mysql-Database所对应的键
    # print(options)
    #
    # items = conf.items("Mysql-Database")  # 获取section名为Mysql-Database所对应的全部键值对
    # print(items)
    #
    # host = conf.get("Mysql-Database", "host")  # 获取[Mysql-Database]中host对应的值
    # print(type(host))
