# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import os

import algorithm
import config

if __name__ == '__main__':
    config.log.info("Crawler is running...")

    #下载pdf
    algorithm.get_PDF_From_Net()