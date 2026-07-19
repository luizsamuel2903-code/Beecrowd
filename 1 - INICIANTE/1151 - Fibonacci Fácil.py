# -*- coding: utf-8 -*-

n = int(input())

termo_1, termo_2 = 0, 1

for i in range(n):
    if i == n-1: print(termo_1, end='-')
    else: print(termo_1, end='+')

    soma_termos = termo_1 + termo_2
    termo_1 = termo_2
    termo_2 = soma_termos
