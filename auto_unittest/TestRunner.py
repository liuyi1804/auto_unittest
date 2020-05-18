# -*- coding:utf-8 -*-
"""
@Title:
@Author: liuyi
@Time:
"""

import os
import unittest
import time,sys

report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports/')
print('report_path:' + report_path)
nowtime = time.strftime("%Y-%m-%d-%H_%M_%S")
htmlfile = report_path + nowtime + 'report.html'

fp = open(htmlfile, 'wb')

# case_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testsuits/')
# case_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'testsuits')
Path= os.path.dirname(os.path.abspath(__file__))
Test_path = os.path.join(Path, 'testsuits')
print(Test_path)
suite = unittest.defaultTestLoader.discover(Test_path, "test*.py", top_level_dir=None)
print(suite)

if __name__ == '__main__':
    # runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=fp, title=u"测试", description=u"情况")
    runner = unittest.TextTestRunner()
    runner.run(suite)
    fp.close()