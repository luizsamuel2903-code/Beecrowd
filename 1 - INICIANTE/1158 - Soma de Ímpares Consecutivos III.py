# -*- coding: utf-8 -*-

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x % 2 == 0: x += 1 

    soma = 0
    for i in range(y):
        soma += x
        x += 2
    print(soma)
    