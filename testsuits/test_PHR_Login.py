"""
@Title:
@Author: liuyi
@Time:
"""
# coding=utf-8
from selenium import webdriver
from time import sleep
import unittest,sys
from os.path import *

sys.path.insert(0,dirname(dirname(abspath(__file__)))) # 返回根目录
from pageobjects.poium_login_page import LoginPage
from framework.browser_engine import BrowserEngine


class TestLogin(unittest.TestCase):

    @classmethod
    def setUp(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)


    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def test_Login(self):
        page = LoginPage(self.driver)
        page.account_input = "admin"
        page.passwd_input = "11111"
        page.login_button.click()
        sleep(5)
        try:
            assert 'manage' in self.driver.current_url
            print("登录成功")
        except Exception as e:
            print('登录失败', format(e))
            page.get_windows_img()

if __name__ == '__main__':
    unittest.main()

