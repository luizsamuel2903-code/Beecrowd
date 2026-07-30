# -*- coding: utf-8 -*-

while True:
    x = int(input())
    if x == 0: break
    for i in range(1, x+1):
        if i != x: print(i, end=' ')
        else: print(i, end='')
    print()

# 00 : 03 : 59, 65
