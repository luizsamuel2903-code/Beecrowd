# -*- coding: utf-8 -*-

matriz = [[0 for _ in range(12)] for _ in range(12)]
coluna, operacao = int(input()), input()

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

resultado = 0
if operacao == 'S':
    for i in range(12):
        resultado += matriz[i][coluna]
if operacao == 'M':
    for i in range(12):
        resultado += matriz[i][coluna]
    resultado /= 12

print(f'{resultado:.1f}')

