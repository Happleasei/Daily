import hanlp
tokenizer = hanlp.load('LARGE_ALBERT_BASE')
fw = open('G:\python\out\_test_hanlp_small_01.csv', 'w', encoding='utf-8')    # 分词结果保存
with open('G:\pycharm\DataSet\_1\_train_small.csv', 'r', encoding='utf-8') as fr:  # 需要分词的文档
    for line in fr:
        line = line.strip()
        word_list = tokenizer(line)
        # print(word_list)
        for term in word_list:    # 分词结果格式：单词和词性。term.word, term.nature：获取单词与词性
            # print(term.word)
            fw.write(term + ' ')
        fw.write('\n')
fw.close()