"""
@Title:
@Author: liuyi
@Time:
"""
# coding=utf-8
import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()

class BrowserEngine():
    """定义一个引擎类"""
    # dir = os.path.dirname(os.path.abspath('.'))
    dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #获取项目所在路径
    # print(dir)
    chrome_driver_path = dir + '/tools/chromedriver.exe'   #拼装驱动路径
    firefox_driver_path = dir + '/tools/geckodriver.exe'
    # webdriver.Firefox(executable_path=self.firefox_driver_path)
    edge_driver_path = dir + '/tools/msedgedriver.exe'

    def __init__ (self, driver):
        self.driver = driver

    def open_browser(self, driver):
        config = configparser.ConfigParser()
        # 拼装配置文件绝对路径
        file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\config\\config.ini'
        print(file_path)
        config.read(file_path)

        browser = config.get("browserType","browserName")
        logger.info(f"You had select {browser} browser.")
        url = config.get("testServer","URL")
        logger.info(f"The test server url is: {url}")
        
        # 判断使用的浏览器
        if browser == 'Firefox':
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == 'Chrome':
            # 初始化实例
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser == 'Edge':
            driver = webdriver.Edge(self.edge_driver_path)
            logger.info("Starting Edge browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        print(driver)
        return driver


    def quit_browser(self):
        logger.info("Now,Close and quit the browser.")
        self.driver.quit()
 
