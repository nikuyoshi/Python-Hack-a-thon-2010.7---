#!/usr/bin/env python
# coding: utf-8 

import sys
import fileinput
import codecs
from datetime import date

argvs = sys.argv[1:]
argc = len(argvs)
# print argvs
# print argc
# print argvs[0]
# print argvs[1]
# print argvs[2]

for i in range(len(argvs)):
    argvs[i] = unicode(argvs[i], 'utf-8')
# print argvs[2]

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
    allLines = open('cashbook.txt').read() 
    print allLines
    #f = open('cashbook.txt', 'r')
    # for line in f:
    #     # test = str(line)
    #     # print line
    #     # print test[0]
    #     # print '---'
    #     itemList = line[:-1].split('\t')
    #     itemList[2] =  
    #     print itemList
    #f.close() 
    print 'a'

if (argvs[0] == 'add'):
    add()
elif (argvs[0] == 'summary'):
    summary()
