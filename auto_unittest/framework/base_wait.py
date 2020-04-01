"""
---------------------------
@Time : 2019/12/3 12:00
@Auth : liuyi1804
@File : base_wait.py
@IDE  : PyCharm、Sublime
@Describe: 等待方法封装
---------------------------
"""
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

class BaseWait(object):
	
	def __init__(self, driver):
		self.driver = driver

	def find_element(self,by,locator,timeout=30):
		"""
		定位单个元素
		by:定位方法，例：By.ID
		locator:定位表达式
		timeout:显示等待超时时间
		return：返回值
		"""
		try:
			element = WebDriverWait(self.driver, timeout).\
				until(lambda driver: driver.find_element(by, locator))
		except (NoSuchElementException,TimeoutException) as e:
			raise e
		else:
			return element
	
		
	def find_elements(self,by,locator,timeout=30):
		"""
		定位一组元素
		by:定位方法，例：By.ID
		locator:定位表达式
		timeout:显示等待超时时间
		return：返回值
		"""
		try:
			elements = WebDriverWait(self.driver, timeout).\
				until(lambda driver: driver.find_elements(by, locator))
		except (NoSuchElementException,TimeoutException) as e:
			raise e
		else:
			return elements
	

if __name__ == '__main__':
	pass