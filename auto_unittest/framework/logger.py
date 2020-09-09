"""
@Title:
@Author: liuyi
@Time:
"""
# coding=utf-8
import logging
import logging.handlers
import os.path
import time

class Logger():

    def __init__(self,logger):
        #创建日志对象
        self.logger = logging.getLogger(logger)
        # 设置日志级别
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handle，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        #错误教训：一行log路径的代码错误，未返回根目录导致log路径拼接错误。
        # log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
        log_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/logs/'
        # print(log_path)
        log_name = log_path + rq + '.log'  #拼装日志名
        # 实例化handler
        fh = logging.handlers.RotatingFileHandler(log_name, maxBytes=1024 * 1024, backupCount=5,
                                                  encoding='utf-8')
        fh.setLevel(logging.INFO) # 设置日志级别为INFO
       
        
        # 再创建一个handler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler 的log输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger
