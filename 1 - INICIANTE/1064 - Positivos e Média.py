# -*- coding: utf-8 -*-

lista_numeros = [float(input()) for _ in range(6)]

total_positivos = 0
lista_positivos = []
for n in lista_numeros:
    if n > 0: 
        total_positivos += 1
        lista_positivos.append(n)
else:
    media = sum(lista_positivos) / total_positivos
    print(f'{total_positivos} valores positivos\n{media:.1f}')

# 00 : 04 : 33
