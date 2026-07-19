# -*- coding: utf-8 -*-

c = int(input())
soma = 0
for i in range(c):
    x, y = map(int, input().split())
    for j in range(x, y+1):
        if j % 2 == 1:
            soma += j
    print(soma)
    soma = 0

