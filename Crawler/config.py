# -*- coding: utf-8 -*-
__author__ = 'root'

import logging

# 脚本日志设置
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s:%(msecs)05.1f pid:%(process)d [%(levelname)s] (%(funcName)s) %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='posCluster.log',
    filemode='a+')
log = logging.getLogger()
