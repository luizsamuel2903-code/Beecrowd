# -*- coding: utf-8 -*-

matriz = [[0 for _ in range(12)] for _ in range(12)]

comando, acumulador, elementos = input(), 0, 0
for i in range(12):
    for j in range(12):
        valor = float(input())
        if i+j>11 and j<6 or i-j>=1 and j>5:
            matriz[i][j] = valor
            acumulador += valor
            elementos += 1
            
if comando == 'S': print(f'{acumulador:.1f}')
if comando == 'M': print(f'{acumulador/elementos:.1f}') 
