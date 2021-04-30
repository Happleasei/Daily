#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import jieba
import jieba.analyse
import xlwt #写入Excel表的库


# def stopwordlist():
#   stopwords = [line.strip() for line in open('G:\python\_files\error_dc\ChangeStopWords.txt').readlines()]
#   return stopwords
word_list = []
if __name__=="__main__":

    fR = open('G:\pycharm\DataSet\_1\_train_big_split_02.csv', 'r')
    sent = fR.read()
    sent_list = jieba.cut(sent)
    # for t in sent_list:
    #     if t not in stopwordlist():
    #         word_list.append(t)
    fW = open('G:\python\out\_test_jieba_big_02.csv', 'w')
    fW.write(' '.join(word_list))

    fR.close()
    fW.close()