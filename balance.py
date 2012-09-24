#!/usr/bin/env python
# -*- coding: utf-8  -*-

import sys
import fileinput
import codecs
from datetime import date

argvs = sys.argv[1:]
argc = len(argvs)
if (argc == 0) :
    print 'Error: wrong number of arguments: 1 and over'
else:
    for i in range(len(argvs)):
        argvs[i] = unicode(argvs[i], 'utf-8')

    def add():
        print
        if (argc != 3) :
            print 'Error: wrong number of arguments: add? requires 3'
        else:
            today = str(date.today())
            f = codecs.open('cashbook.txt','a+','utf-8')
            f.write(today+'\t'+ argvs[1] +'\t'+argvs[2]+'\n')
            f.close()

    def summary():
        f = open('cashbook.txt', 'r')
        ################################################
        # itemList = []
        # for line in f:
        #     itemList.append( line[:-1].split('\t') )
        # print itemList
        ################################################
        # ↑をリスト内包表記に書き換え、タブ・改行を無くしてリストに入れる
        itemList = [line[:-1].split('\t') for line in f]
        date = {} 
        for x in range(len(itemList)):
            if itemList[x][0] in date:
                 date[itemList[x][0]] += int(itemList[x][1])
            else :
                 date[itemList[x][0]] = int(itemList[x][1])
        for (i, j) in date.items():
            print '%s \t %d' %(i, j)

    def application():
        f = open('cashbook.txt', 'r')
        itemList = [line[:-1].split('\t') for line in f]
        app = {} 
        for x in range(len(itemList)):
            if itemList[x][2] in app:
                 app[itemList[x][2]] += int(itemList[x][1])
            else :
                 app[itemList[x][2]] = int(itemList[x][1])
        for (i, j) in sorted(app.items(), key=lambda x:x[1], reverse=True):
            print '%s \t %d' %(i, j)

        
    if (argvs[0] == 'add'):
        add()
    elif (argvs[0] == 'summary'):
        summary()
    elif (argvs[0] == 'application'):
        application()
