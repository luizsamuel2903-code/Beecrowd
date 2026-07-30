# -*- coding: utf-8 -*-

matriz = [[0 for _ in range(12)] for _ in range(12)]
linha, operacao = int(input()), input()
for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())
if operacao == 'S': print(sum(matriz[linha]))
if operacao == 'M': print(sum(matriz[linha])/12)
