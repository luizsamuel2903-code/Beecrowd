# -*- coding: utf-8 -*-

n = int(input())

termo_1, termo_2 = 0, 1

for i in range(n):
    print(termo_1)
    soma_termos = termo_1 + termo_2
    termo_1 = termo_2
    termo_2 = soma_termos
