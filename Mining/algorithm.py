# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import codecs
import jieba
import nltk
import gensim
import zhon.hanzi
import zhon.pinyin
import os
import re

import config


def init(jieba_parallel=False):
    # 加载英语/中文停止词,分别来自nltk和zhon
    global english_stopwords, chinese_stopwords
    english_stopwords = set(nltk.corpus.stopwords.words('english'))
    chinese_stopwords = {word[:-1] for word in codecs.open("stopwords.txt", "r", encoding="utf-8")}

    # 设置结巴分词log级别
    jieba.setLogLevel("INFO")
    # 设置结巴分词字典文件
    jieba.set_dictionary("./jieba_dict.txt")
    # 修改结巴分词临时工作目录
    jieba.tmp_dir = os.getcwd()
    # 开启并行分词模式，进程数为CPU核心数
    if jieba_parallel:
        jieba.enable_parallel()

    config.log.info("module algorithm has initialized successfully.")


def calculate(first_treat=False, raw_pos_random=None):
    # 设置输出输入,输出文件
    if not first_treat:
        output_dir = "./txt/"
        input_dir = "../Crawler/txt/"
        for index in range(1, 49):
            text_file = codecs.open(output_dir + str(index) + ".txt", 'w', encoding='utf-8')
            inputfp = codecs.open(input_dir+str(index)+".txt", 'rb', encoding='utf-8')

            # 初步处理,去掉 本科课程介绍 这句话
            for line in inputfp:
                if not re.match(".*2014-2015 学年度本科课程介绍 ", line):
                    text_file.write(line[:-1])

            text_file.close()
            inputfp.close()

    global dictionary, corpus

    # 抽取词袋
    input_dir = "./txt/"
    for index in range(1, 49):
        inputfp = open(input_dir+str(index)+'.txt')
        dictionary = gensim.corpora.Dictionary(inputfp)

    # 建立用词频表示的文档向量
    corpus = [dictionary.doc2bow(text) for text in inputfp]

    # 建立tfidf模型
    __build_tfidf()

    # 建立lsi模型
    __build_lsi()


def __build_tfidf():
    global tfidf, corpus_tfidf
    # 建立TF-IDF模型
    tfidf = gensim.models.TfidfModel(corpus)

    # 建立用TF-IDF值表示的文档向量
    corpus_tfidf = tfidf[corpus]

def __build_lsi():
    global lsi, index
    # 建立LSI模型
    lsi = gensim.models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=100)

    # 建立相似度索引
    index = gensim.similarities.MatrixSimilarity(lsi[corpus])