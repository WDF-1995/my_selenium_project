# # -*- coding:utf-8 -*-
# """
# @Auth：Richard
# @Time：2021年12月08日
# """
#
# # encoding:utf-8
# import re
#
# import requests
# import base64
#
# '''
# 通用文字识别（高精度版）
# '''
#
#
# def read_picture(picture):
#     """识别图片验证码"""
#     # 调用三方API识别验证码
#     request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
#     # 二进制方式打开图片文件
#     f = open(picture, 'rb')
#     img = base64.b64encode(f.read())
#     params = {"image": img}
#     access_token = '24.6fe3cfb7cd27499f4bfa5af83edc27ff.2592000.1641528021.282335-25304772'
#     request_url = request_url + "?access_token=" + access_token
#     headers = {'content-type': 'application/x-www-form-urlencoded'}
#     response = requests.post(request_url, data=params, headers=headers)
#     code = re.sub("\D", "", response.json()['words_result'][0]['words'])
#     f.close()
#     return code
