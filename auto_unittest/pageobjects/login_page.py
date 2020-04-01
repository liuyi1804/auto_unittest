import time,unittest,sys
from selenium import webdriver
from os.path import dirname,abspath

# 继承基类之前把对应目录加入path
sys.path.append("../framework/")
from framework.base_page import BasePage

class LoginPage(BasePage):
	""" 登录页封装操作的元素"""
	url = 'http://dev.aijiayi.com/'

	def account_input(self,account):
		self.by_xpath("//*[@class='el-input__inner' and @type='text']").send_keys(account)

	def passwd_input(self,password):
		self.by_xpath("//*[@class='el-input__inner' and @type='password']").send_keys(password)

	def login_button(self):
		self.by_xpath("//*[@class='el-button el-button--primary el-button--large']").click()
