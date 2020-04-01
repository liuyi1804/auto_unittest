from selenium.common.exceptions import NoSuchWindowException
import time,sys
from os.path import *

# sys.path.insert(0,dirname(dirname(abspath(__file__)))) # 返回根目录的方法
sys.path.append("../framework/")
from framework.logger import Logger # 导入logger中的Logger类

# 创建日志
logger = Logger(logger='BasePage').getlog()

class BasePage():
	"""
	基础层封装常用方法
	"""
	def __init__(self,driver):
		self.driver = driver

	# 退出浏览器
	def quit_browser(self,driver):
		self.driver = driver

	# id定位
	def by_id(self,id_):
		return self.driver.find_element_by_id(id_)

	# name定位
	def by_name(self,name):
		return self.driver.find_element_by_name(name)

	# xpath定位
	def by_xpath(self,xpath):
		return self.driver.find_element_by_xpath(xpath)

	# class定位
	def by_class(self,class_name):
		return self.driver.find_element_by_class_name(class_name)

	# css定位
	def by_css(self,css):
		return self.driver.find_element_by_css_seletor(css)
	
	# 获取title
	def get_title(self):

		return self.driver.title

	# 获取url
	def get_url(self):
		return self.driver.current_url

	# 获取页面TEXT,仅使用xpath
	def get_text(self,xpath):
		return self.by_xpath(xpath).text

	# 执行JS脚本
	def js(self,script):
		self.driver.execute_script(script)