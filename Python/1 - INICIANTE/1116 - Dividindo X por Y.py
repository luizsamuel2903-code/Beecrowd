# -*- coding: utf-8 -*-

r = int(input())
for i in range(r):
    x, y = map(int, input().split())
    try:
        resultado = x / y
        print(round(resultado, 1))
    except:
        print('divisao impossivel')

# 00 : 03 : 58, 18
