# -*- coding: utf-8 -*-

lista_numeros = [int(input()) for _ in range(5)]

for n in lista_numeros:
    if n % 2 != 0:
        lista_numeros.remove(n)

print(f'{len(lista_numeros)} valores pares')

# 00 : 03 : 44
