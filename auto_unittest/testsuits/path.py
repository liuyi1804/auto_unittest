# -*- coding:utf-8 -*-
"""
@Title:
@Author: liuyi
@Time:
"""

import os.path

# base_dir = os.path.dirname(os.getcwd())
# os.getcwd() 定位路径为testsuits
# os.path.dirname(os.getcwd())    定位路径为auto_unittest

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
# os.path.abspath(__file__)   定位为path.py路径
# os.path.dirname(os.path.abspath(__file__))  定位为testsuits路径
# os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 定位为auto_unittest路径