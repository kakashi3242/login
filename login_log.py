#coding=utf8

import logging
import time


# 创建一个logger
logger = logging.getLogger('Login Pressure')
logger.setLevel(logging.DEBUG)
# 创建一个handler，用于写入日志文件
file_name = str(time.ctime()) + ' login.log'
fh = logging.FileHandler(file_name, encoding = 'utf-8')
fh.setLevel(logging.INFO)
# 再创建一个handler，用于输出到控制台
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# ch.setFormatter(formatter)
# 给logger添加handler
logger.addHandler(fh)
# logger.addHandler(ch)
# 记录一条日志
# name = 'ssss'
# error = '错的'
# logger.info('nihaoma')
# logger.warning(name)
# logger.error(error)

