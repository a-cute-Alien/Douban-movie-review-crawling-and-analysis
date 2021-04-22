#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Author       : Wu ZiChun
 @CreateTime   : 2021/4/20 22:06 
 @File         : test.py
 @Version      : v1.0.0
 @Description  :
"""
# 按文本字符串分析
from cemotion import Cemotion
import matplotlib
from matplotlib import pyplot as plt
from collections import Counter

matplotlib.rc("font", family='YouYuan')  # 设置字体 支持显示中文


# 获得情感分数 将情感分数保存到scores_list，将情感分级保存到like_list， 情感频率保存到count_list
def getEmotionScore(filename):
    c = Cemotion()  # 使用Cemotion()库
    scores_list = []
    like_list = [0, 0, 0]
    with open(filename, 'r', encoding='utf-8') as f:
        comments = f.readlines()
        f.close()
    for con in comments:
        score = c.predict(con.strip())  # 通过NPL求得预测的情感分数
        scores_list.append(score)
        if score <= 0.4:
            like_list[0] += 1
        elif score >= 0.6:
            like_list[2] += 1
        else:
            like_list[1] += 1
    count_list = Counter(scores_list)
    return scores_list, like_list, count_list


# 通过使用matplotlib库及那个情感分析情况可视化
def showScore(like_list, scores_list):
    fig, axe = plt.subplots(ncols=2, nrows=1, figsize=(20, 7))

    labels = '不喜欢', '一般', '喜欢'
    colors = ['#fa2020', '#20fa91', '#0085ff']
    axe[0].set_title("情感分布", fontsize=18)
    axe[0].pie(x=like_list,
               labels=labels,
               autopct='%1.1f%%',
               textprops={'fontsize': 18},
               shadow=True,
               explode=(0.1, 0, 0),
               colors=colors)

    axe[1].set_title("情感频度图", fontsize=18)
    axe[1].set_xlabel('分数')
    axe[1].set_ylabel('频度')
    axe[1].hist(scores_list, 50)
    plt.show()


if __name__ == '__main__':
    scores, like, count = getEmotionScore("comments_short.txt")
    showScore(like, scores)
