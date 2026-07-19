# -*- coding: utf-8 -*-

for i in range(int(input())):
    x, y = map(int, input().split())
    soma = 0
    for i in range(y):
        if x % 2 == 0:
            soma += x + i
    print(soma)