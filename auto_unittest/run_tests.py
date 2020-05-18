# coding=utf-8
import time
import os, sys
import unittest
import yagmail
from lib import HTMLTestRunner_PY3
# from BeautifulReport import BeautifulReport

def send_mail(html_path):
    yag = yagmail.SMTP(user="lywingpengyou@126.com", #发件人邮箱
                       password="TSWBDEUWZTJDMOFN", #对应邮箱授权码
                       host="smtp.126.com")
    contents = ['PHR运营端测试报告',
                '系统自动发送，请勿回复！']
    # 接收人邮箱、邮件名
    yag.send('lywingpengyou@126.com','UI-TestReport(PHR)',contents, [html_path])
    print('发送成功！')

report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports/')
# print(report_path)
now_time = time.strftime("%Y-%m-%d-%H_%M_%S") # 当前时间
html_name = './reports/' + now_time + "report.html" # 生成报告名称
fp = open(html_name, 'wb') # 打开报告读取数据

# 用例路径
Path= os.path.dirname(os.path.abspath(__file__)) # 返回项目路径
Test_path = os.path.join(Path, 'testsuits') # 拼接用例绝对路径
print('Test_path：'+ Test_path)

# discover方法，执行指定目录下的所有test开头的py文件
test_suite = unittest.defaultTestLoader.discover(Test_path, pattern="test_*.py", top_level_dir=None)
# print('test_suite：'+ test_suite)
print("测试报告", html_name)


if __name__ == '__main__':
    runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=fp, title="PHR运营端测试报告", description="用例测试情况")
    # runner = unittest.TextTestRunner()
    runner.run(test_suite)
    fp.close()
    send_mail(html_name)
    
