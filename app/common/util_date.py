# -*- coding:utf-8 -*-
__author__ = 'snake'

import random
from datetime import datetime


def decode_result_date(datas):
    """
    将数据库查询的数据进行时间格式化
    :param datas: (())， 从数据库查询的数据
    :return: [[]] 返回list列表
    """
    results = []
    for data in datas:
        tmp_list = []
        for item in data:
            if isinstance(item, datetime):
                tmp_list.append(item.strftime('%Y-%m-%d %H:%M:%S'))
            else:
                tmp_list.append(item)
        results.append(tmp_list)

    return results


def get_current_time():
    """
    获取当前时间
    :renturn:"2018-03-20 17:30:56"
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_token():
    '''
    生成登陆后的token，格式如下：
    "9200166a-100b-4808-9ead-7dcb698a5060"
    '''
    codelist = 'abcdefghijklmnopqrstuvwxyz1234567890'
    code1 = ""
    for i in range(8):
        code = random.choice(codelist)
        code1 += code
    code2 = ""
    for i in range(4):
        code = random.choice(codelist)
        code2 += code
    code3 = ""
    for i in range(4):
        code = random.choice(codelist)
        code3 += code
    code4 = ""
    for i in range(4):
        code = random.choice(codelist)
        code4 += code
    code5 = ""
    for i in range(12):
        code = random.choice(codelist)
        code5 += code
    token = code1 + "-" + code2 + "-" + code3 + "-" + code4 + "-" + code5
    return token
