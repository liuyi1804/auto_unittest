from selenium.common.exceptions import NoSuchWindowException
import time,sys
import os.path

# sys.path.insert(0,dirname(dirname(abspath(__file__)))) # 返回根目录的方法
sys.path.append("../framework/")
from framework.logger import Logger # 导入logger中的Logger类
from selenium.common.exceptions import NoSuchElementException

# 创建日志
logger = Logger(logger='BasePage').getlog()

class BasePage():
	"""
	基础层封装常用方法
	"""
	def __init__(self,driver):
		self.driver = driver

	# 退出浏览器
	def quit_browser(self):
		self.driver.quit()

	# 浏览器前进
	def forward(self):
		self.driver.forward()
		logger.info("Click forward on current page.")

	# 浏览器后退
	def back(self):
		self.driver.back()
		logger.info("Click back on current page.")

	# 隐式等待
	def wait(self,seconds):
		self.driver.implicitly_wait(seconds)
		logger.info(f"wait for {seconds} seconds.")

	# 关闭当前窗口
	def	close(self):
		try:
			self.driver.close()
			logger.info("Closing and quit the windows.")
		except NameError as e:
			logger.info(f"Failed to quit the window with {e}")

	# 保存图片
	def get_windows_img(self):
		file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
	 
		rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
		screen_name = file_path + rq + '.png'
  
		try:
			self.driver.get_screenshot_as_file(screen_name)
			logger.info("Had take screenshot and save to folder : /screenshots")
		except NameError as e:
			logger.error(f"Failed to take screenshot! {e}")
			self.get_windows_img()
			
	# 定位元素方法
	def find_element(self, selector):
		'''避免表达式中有=时切割不准的问题,用=>区分'''
		element = ''
		if '=>' not in selector:
			return self.driver.find_element_by_id(selector)
		selector_by = selector.split('=>')[0] # split切割函数，以=>来切割字符串，并把第0个赋值给变量
		selector_value = selector.split('=>')[1]
		print(selector_value)
		
		#定位方法中有‘i’或‘id’
		if selector_by == 'i' or selector_by == 'id':
		#判断是否定位到元素，重新赋值并打印日志
			try:
				element = self.driver.find_element_by_id(selector_value)
				logger.info(f"Had find the element {element.text} successful "
							f"by {selector_by} via value: {selector_value}")
			except NoSuchElementException as e:
				logger.error(f"NoSuchElementException: {e}")
				self.get_windows_img()
		elif selector_by == 'n' or selector_by == 'name':
			element = self.driver.find_element_by_name(selector_value)
		elif selector_by == 'c' or selector_by == 'class':
			element = self.driver.find_element_by_class(selector_value)
		elif selector_by == 'l' or selector_by == 'link_text':
			element = self.driver.find_element_by_link_text(selector_value)
		elif selector_by == 'p' or selector_by == 'partial_link_text':
			element = self.driver.find_element_by_partial_link_text(selector_value)
		elif selector_by == 't' or selector_by == 'tag_name':
			element = self.driver.find_element_by_tag_name(selector_value)
		elif selector_by == 'x' or selector_by == 'xpath':
			try:
				element = self.driver.find_element_by_xpath(selector_value)
				logger.info(f"Had find the element {element.text} successful "
							f"by {selector_by} via value: {selector_value}")
			except NoSuchElementException as e:
				logger.error(f"NoSuchElementException:{e}")
				self.get_windows_img()
		elif selector_by == 's' or selector_by == 'selector_selector':
			element = self.driver.find_element_by_css_selector(selector_value)
		# 若定位不到元素，则通过raise手动抛出异常提醒，并停止执行
		else:
			raise NameError("Please enter valid positioning element.")
		print(element)
		return element
				
				
				
	# 获取title
	def get_title(self):
		return self.driver.title
	
	# 执行JS脚本
	def js(self, script):
		self.driver.execute_script(script)
		
	# 输入
	def type(self, selector, text):
		el = self.find_element(selector)
		el.clear()
		try:
			el.send_keys(text)
			logger.info(f"Had type {text} in inputBox")
		except NameError as e:
			logger.error(f"Failed to type in input box with {e}.")
			self.get_windows_img()
	
	# 清除文本
	def clear(self, selector):
	# 将封装的定位方法赋值给变量
		el = self.find_element(selector)
		try:
			el.clear()
			logger.info("Clear text in input before typing.")
		except NameError as e:
			logger.error("Failed to clear in input box with %s " % e)
		self.get_windows_img()
		
	# 点击
	def click(self, selector):
		el = self.find_element(selector)
		try:
			el.click()
			logger.info(f"The element {el} was clicked.")
		except NameError as e:
			logger.info(f"Failed to click the element with {e}")
			
	# 声明独立的静态方法
	@staticmethod
	def sleep(seconds):
		time.sleep(seconds)
	
		
		
	# 定位方式封装
	# def by_id(self,id_):
	# 	return self.driver.find_element_by_id(id_)
	# def by_name(self,name):
	# 	return self.driver.find_element_by_name(name)
	# def by_xpath(self,xpath):
	# 	return self.driver.find_element_by_xpath(xpath)
	# def by_class(self,class_name):
	# 	return self.driver.find_element_by_class_name(class_name)
	# def by_css(self,css):
	# 	return self.driver.find_element_by_css_seletor(css)
	# def get_url(self):
	# 	return self.driver.current_url
	# def get_text(self,xpath):
	# 	return self.by_xpath(xpath).text
	
