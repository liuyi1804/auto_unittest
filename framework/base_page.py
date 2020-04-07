from selenium.common.exceptions import NoSuchWindowException
import time,sys
import os.path

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
		screent_name = file_path + rq + '.png'
  
		try:
			self.driver.get_screentshot_as_file(screent_name)
			logger.info("Had take screenshot and save to folder : /screenshots")
		except NameError as e:
			logger.error(f"Failed to take screentshot! {e}")
			self.get_windows_img()
   
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