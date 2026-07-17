# -*- coding: utf-8 -*-

n = int(input())

for i in range(n):
    impares = 0
    entrada = map(int, input().split())
    menor, maior = sorted(entrada)
    for j in range(menor+1, maior):
        if j % 2 != 0:
            impares += j
    print(impares)
    
# 00 : 07 : 03, 27
