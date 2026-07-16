# -*- coding: utf-8 -*-

numeros = [int(input()) for _ in range(2)]
menor, maior = sorted(numeros)

soma_impares = 0
for n in range(menor + 1, maior):
    if n % 2 != 0:
        soma_impares += n
print(soma_impares)

# 00 : 02 : 29, 14
