# -*- coding:utf-8 -*-
"""
@Auth：Richard
@Time：2021年12月08日
"""

import pickle
import random
import re
import smtplib

import string
import os

import logging
import logging.handlers
import datetime
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import redis


def gen_random_str():
    """生成随机字符串"""
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return rand_str


def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        cookies = driver.get.cookies()
        print(cookies)
        pickle.dump(cookies, filehandler)


def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)


def get_logger():
    """日志"""
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # all文件设置
        all_log = os.path.dirname(os.path.dirname(__file__)) + '\\logs' + '\\all.log'
        rf_handler = logging.handlers.TimedRotatingFileHandler(all_log, when='midnight', interval=1, backupCount=7,
                                                               atTime=datetime.time(0, 0, 0, 0))
        rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

        # error错误文件设置
        error_log = os.path.dirname(os.path.dirname(__file__)) + '\\logs' + '\\error.log'
        f_handler = logging.FileHandler(error_log)
        f_handler.setLevel(logging.ERROR)
        f_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

        # 控制台输出日志
        c_handler = logging.StreamHandler()
        c_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

        logger.addHandler(rf_handler)
        logger.addHandler(f_handler)
        logger.addHandler(c_handler)
    return logger


def send_mail(file_new):
    """发送邮件"""
    f = open(file_new, 'rb')
    # 读取测试报告正文
    mail_body = f.read()
    f.close()

    # 发送邮箱服务器
    smtp_server = "smtp.exmail.qq.com"
    # 发件人邮箱
    sender = 'wanghua@fintoptech.com'
    # 发件人邮箱密码
    password = '3PVwHpHzE4RAG!N'
    # 接收人邮箱
    receiver = ['wanghua@fintoptech.com']

    # 通过  模块构造的带附件的邮件如图
    msg = MIMEMultipart()

    # 发送正文
    text = '测试执行结束；\n附件为本次测试结果，请下载至本地查阅(未下载至本地会导致部分数据无法正常加载)。'
    text = MIMEText(text, 'plain', 'utf-8')
    msg['Subject'] = Header('AutoTestReport', 'utf-8')
    msg.attach(text)
    # Header()用于定义邮件标题

    # 发送附件
    msg_file = MIMEText(mail_body, 'html', 'utf-8')
    msg_file['Content-Type'] = 'application/octet-stream'
    msg_file["Content-Disposition"] = 'attachment; filename="AutoTestReport.html"'
    msg.attach(msg_file)

    smtp = smtplib.SMTP_SSL(smtp_server)
    smtp.connect(smtp_server, port=465)
    smtp.login(sender, password)  # 登录的用户名和密码
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


def get_code():
    conn = redis.Redis(host='120.25.153.60', password='X%lbXSj^d*svS#KJQt8KkZKhcjZMD', port='6379', db=13)
    keys = conn.keys(pattern='code-key*')
    # 获取最新的验证码
    lst = []
    for i in keys:
        key = bytes.decode(i)
        code = bytes.decode(conn.get(key))
        t = conn.pttl(key)
        lst.append((t, code))
    return re.sub("\D", "", max(lst)[1])

# def find_element_wait(driver, *locator, timeout=15):
#     """
#         方法：动态查找元素，显式等待
#         参数：
#             locator：元素定位的方式和值
#                 - ('id', 'kw')                      # driver.find_element_by_id('kw')
#                 - ('xpath', 'xxxxx')
#                 - ('name', 'xxx')
#                 - ('css selector', 'xxxx')
#                 - ('class name', 'xxxx')            # driver.find_element_by_class_name
#                 - ('link text', 'xxxx')             # driver.find_element_by_link_text
#                 - ('partial link text', 'xxx')      # driver.find_element_by_partial_link_text
#             timeout：找元素的超时时间，默认60
#         返回值：
#             找到元素就返回元素，没有做找到元素就报错，timeout
#     """
#     return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))