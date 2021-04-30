#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：WangHai_Python -> 10_CutSmallDataSet
@IDE    ：PyCharm
@Author ：Wang hai
@Date   ：2021/4/6 10:14
@Desc   ：
=================================================='''

fR = open('F:/StudyFiles/pycharm/DataSet/XLnet/Train.txt', 'r', encoding='utf-8')
fW = open('F:/StudyFiles/pycharm/DataSet/XLnet/1/Train.txt', 'w')

sent = fR.read()
for i,t in enumerate(sent):
    if i <= 2029935 :
        fW.write(t)

fR.close()
fW.close()
