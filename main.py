#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Author       : Wu ZiChun
 @CreateTime   : 2021/4/21 23:46 
 @File         : main.py
 @Version      : v1.0.0
 @Description  :
"""
from get.get_long_comments import getLcomment
from get.get_short_comments import getScomment
from show.show_word_cloud import showWordCloud
from show.emotion_analysis import getEmotionScore, showScore

if __name__ == '__main__':
    mvid = input('电影的id为：')
    getLcomment(mvid, "long.txt")
    getScomment(mvid, "short.txt")
    showWordCloud("long.txt")
    scores, like, count = getEmotionScore("short.txt")
    showScore(like, scores)
