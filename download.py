#!/usr/bin/python
# coding: UTF-8
import os

f = open('urls.txt')
lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()
# lines: リスト。要素は1行の文字列データ

for line in lines:
    os.system("wget "+ line),
print
