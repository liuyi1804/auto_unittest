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
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handle，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        #一行log路径的代码错误，搞了几天。
        # log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
        log_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/logs/'
        print(log_path)
        log_name = log_path + rq + '.log'  #拼装日志名
        # 实例化handler
        fh = logging.handlers.RotatingFileHandler(log_name, maxBytes=1024 * 1024, backupCount=5,
                                                  encoding='utf-8')
        fh.setLevel(logging.INFO)
       
        
        # 再创建一个handler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler 的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger
