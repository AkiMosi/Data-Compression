# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
j=0
final=''
f = open('normal.txt','r+')
q=open('bin.txt','w')
a=f.readline()
b=[]
for i in a:
    c=int(ord(i))
    b.append(bin(c))
for i in range(0, len(a)):
    m=str(b[0])
    m=m[2:]
    final=final+m
q.writelines(final)
f.close()
q.close()