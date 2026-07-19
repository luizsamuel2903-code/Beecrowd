# -*- coding: utf-8 -*-

x, y = map(int, input().split())

z = 1
while z < y:
    for i in range(x):
        if i+1 != x: print(z, end=' ')
        else: print(z, end='')
        z += 1
    print()
