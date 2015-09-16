# -*- coding: utf-8 -*-
__author__ = 'root'

import urllib
import os

#获取清华课程表及其介绍的PDF
def get_PDF_From_Net():
    # 设置存储目录
    local_dir = "./pdf/"

    # PDF文件的url模板
    basic_url_front = "http://www.tsinghua.edu.cn/publish/newthu/newthu_cnt/education/pdf/edu-1-2/2015_"
    basic_url_tail = ".pdf"

    # 下载PDF文件
    for index in range(1, 48):
        # 设置文件url
        file_url = ''.join([basic_url_front, str(index), basic_url_tail])
        print file_url
        # 设置文件名
        local_pdf = ''.join([local_dir, str(index), basic_url_tail])
        try:
            # 下载
            urllib.urlretrieve(file_url, local_pdf)
        except:
            continue

#
def PDF_to_TXT(index):
