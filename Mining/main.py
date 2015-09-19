# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import algorithm
import config

if __name__ == '__main__':
    # 启动记录
    config.log.info("Mining is running")

    # 初始化
    algorithm.init()
    algorithm.calculate(config.first_treat)
