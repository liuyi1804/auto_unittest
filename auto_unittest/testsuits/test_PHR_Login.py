"""
@Title:
@Author: liuyi
@Time:
"""
# coding=utf-8
from parameterized import parameterized
from time import sleep
import unittest
import os.path

# sys.path.insert(0,dirname(dirname(abspath(__file__)))) # 添加根目录
# os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 返回根目录

# from pageobjects.poium_login_page import LoginPage #导入由poium封装的登录页
from framework.browser_engine import BrowserEngine # 导入普通封装的登录页
from pageobjects.login_page import LoginPage


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 参数化登录账号名和密码
    @parameterized.expand([
        ("user", "123456"),
        ("admin", "111111"),
    ])
    def test_Login(self, account, password):
        page = LoginPage(self.driver)
        page.account_input(account)
        page.password_input(password)
        page.login_button()
        sleep(5)
        try:
            assert 'manage' in self.driver.current_url
            print("登录成功")
        except Exception as e:
            print('登录失败', format(e))
            page.get_windows_img()

if __name__ == '__main__':
    unittest.main(verbosity=2)

