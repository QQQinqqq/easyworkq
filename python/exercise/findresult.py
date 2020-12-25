#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
def to4(x):
    list=[]
    while x>3:
        list.append(str(x%4))
        x=x//4
    if x:
        list.append(str(x))
    x=''.join(reversed(list))
    x=x.zfill(10)
    return x

def judge(x):
    minS = min('0123',key=x.count)
    maxS = max('0123',key=x.count)
    n = [int(i) for i in x]
    select2 = '2301'
    if select2[n[1]] != x[4]:
        return False
    select3 = '2513'
    temp = select3.replace(select3[n[2]],'')
    if n[2] == int(temp[0]):
        return False
    if n[int(temp[0])] != n[int(temp[1])]:
        return False
    if n[int(temp[0])] != n[int(temp[2])]:
        return False
    select4 = [(0,4),(1,6),(0,8),(5,9)]
    temp=select4[n[3]]
    if n[temp[0]] != n[temp[1]]:
        return False
    select5 = '7386'
    if n[4] != n[int(select5[n[4]])]:
        return False
    select6 = [(1,3),(0,5),(2,9),(4,8)]
    temp = select6[n[5]]
    if n[7] != n[int(temp[0])]:
        return False
    if n[7] != n[int(temp[1])]:
        return False
    select7 = '2103'
    if select7[n[6]] != minS:
        return False
    select8 = '6419'
    if abs(n[0]-n[int(select8[n[7]])])<=1:
        return False
    select9 = '5918'
    if n[0] == n[5]:
        if n[int(select9[n[8]])] == n[4]:
            return False
    if n[0] != n[5]:
        if n[int(select9[n[8]])] != n[4]:
            return False
    select10 = '3241'
    if int(select10[n[9]]) != (x.count(maxS)-x.count(minS)):
        return False
    return True

for x in range(int(math.pow(4,10))):
    x = to4(x)
    if judge(x):
        print("".join([chr(65+int(i)) for i in x]))
