import jieba

fR = open('G:\pycharm\DataSet\_1\_train_big.csv', 'r',encoding='utf-8')
sent = fR.read()
sent_list = jieba.cut(sent)
fW = open('G:\pycharm\DataSet\_1\_train_big_05.csv', 'w',encoding='utf-8')
fW.write(' '.join(sent_list))
fR.close()
fW.close()