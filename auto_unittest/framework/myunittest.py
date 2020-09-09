# -*- coding:utf-8 -*-
"""
@Title:
@Author: liuyi
@Time:
"""

from time import sleep
import unittest
from framework.browser_engine import BrowserEngine


class Myunit(unittest.TestCase):
  

    @classmethod
    # 错误教训：setUpClass写成setupClass。
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
    # def setUp(self):
    #     browse = BrowserEngine(self)
    #     browse.open_browser(self)
    
    
    # def tearDown(self):
    #    self.driver.quit()
     
if __name__ == '__main__':
    unittest.main(verbosity=2)



        

        
        

 
        


