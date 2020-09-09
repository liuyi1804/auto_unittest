# import sys
#
# # 继承基类之前把对应目录加入path
# sys.path.append("../framework/")
from framework.base_page import BasePage

class LoginPage(BasePage):
	""" 登录页封装操作的元素"""
	account = "xpath=>//*[@class='el-input__inner' and @type='text']"
	password = "xpath=>//*[@class='el-input__inner' and @type='password']"
	login_btn = "xpath=>//*[@class='el-button el-button--primary el-button--large']"
	
	# 账号输入
	def account_input(self, text):
		self.type(self.account, text)

	def password_input(self, text):
		self.type(self.password, text)

	def login_button(self):
		self.click(self.login_btn)
	
	# 公共登录方法
	def loginFunc(self, account='admin', password='123456'):
		self.account_input(account)
		self.password_input(password)
		self.login_button()
