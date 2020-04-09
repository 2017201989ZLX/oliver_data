
# -*-coding:utf-8 -*-
import os
import csv
import codecs
import jieba
import jieba.posseg as pseg
import re
def get_data(filename):
    try:
        txt = open(filename, encoding="utf-8").read()
    except:
        txt = open(filename,encoding='GB2312').read()
    pattern="[\u4e00-\u9fa5]+" 
    regex = re.compile(pattern)
    results = regex.findall(txt)
    txt = "".join(results)

    cixing = pseg.lcut(txt)
    count  = jieba.lcut(txt)
    word_count = {}
    word_flag = {}
    word_data = []

    for w in cixing:
        word_flag[w.word] = w.flag
    for word in count:
        if len(word) == 1:
            continue
        else:
            word_count[word] = word_count.get(word, 0) + 1
    items = list(word_count.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in items:
        if i[1] == 1:
            continue
        else:
            word_data.append(i[0]+"("+str(i[1])+")")
    return word_data


import pandas as pd
word_datas = []
# temp = get_data("anlian.txt")
# print(len(temp))
# word_datas.append(get_data("anlian.txt"))
# word_datas.append(get_data("guangda.txt"))
# word_datas.append(get_data("zhifubao.txt"))
word_datas.append(get_data("11.txt"))
word_datas = [[row[i] for row in word_datas] for i in range(len(word_datas[0]))]
name=['微医保终身重疾']
test=pd.DataFrame(columns=name,data=word_datas)
# # print(test)
test.to_csv('data_3.csv',encoding='GB2312')
