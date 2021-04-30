# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP

def stopwordlist():
  stopwords = [line.strip() for line in open('G:\python\_files\error_dc\ChangeStopWords.txt', encoding='UTF-8').readlines()]
  return stopwords
word_list = []
fR = open('G:\pycharm\DataSet\_1\_train_small.csv', 'r',encoding='utf-8')
nlp = BosonNLP('your API token')
sent = fR.read()
sent_list = nlp.tag(sent)
for t in sent_list:
    if t not in stopwordlist():
        word_list.append(t)
fW = open('G:\python\out\_test_jieba_big_02.csv', 'w')
fW.write(' '.join(word_list))

fR.close()
fW.close()
    
    
    