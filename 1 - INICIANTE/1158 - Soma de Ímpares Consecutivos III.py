# -*- coding: utf-8 -*-

c = int(input())
for i in range(c):
    soma = 0
    x, y = map(int, input().split())

    for j in range(y):
        if j % 2 != 0:
            soma += j
    print(soma)
