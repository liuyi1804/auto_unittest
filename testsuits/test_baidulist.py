"""
---------------------------
@Time :
@Auth : liuyi1804
@File : test_baidulist.py
@IDE  : PyCharm、Sublime
@Describe: baidu搜索并打印功能
---------------------------
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest,sys,time
from os.path import dirname,abspath
sys.path.append("../framework/")
from framework.base_wait import BaseWait
from framework.browser_engine import BrowserEngine

class BaiduList(unittest.TestCase):
    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_baidu_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。

        """
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        self.driver.find_element_by_id('su').click()
        time.sleep(5)
        try:
            assert 'selenium' in self.driver.title
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))



if __name__ == '__main__':
    unittest.main()

