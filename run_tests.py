# coding=utf-8
import time
import unittest
import yagmail
from lib.HTMLTestRunner_PY3 import HTMLTestRunner

def send_mail(html_path):
    yag = yagmail.SMTP(user="lywingpengyou@126.com",
                       password="TSWBDEUWZTJDMOFN",
                       host="smtp.126.com")
    contents = ['PHR运营端测试报告']
    yag.send('lywingpengyou@126.com','HTML测试报告',contents, [html_path])
    print('发送成功！')

# discover方法，执行指定目录下的所有test开头的py文件
suit = unittest.defaultTestLoader.discover("./testsuits","test_*.py")
# 当前时间
now_time = time.strftime("%Y-%m-%d-%H_%M_%S")
html_path = "./reports/" + now_time + "report.html"
print("测试报告", html_path)
fp = open(html_path, "wb")
runner = HTMLTestRunner(stream=fp,
                        title="PHR运营端回归测试报告",
                        description="运行环境：Windows 10, Chrome/FireFox")

runner.run(suit)
fp.close()
send_mail(html_path)