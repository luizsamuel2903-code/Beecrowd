# -*- coding: utf-8 -*-

numeros = [int(input()) for _ in range(2)]

menor, maior = sorted(numeros)
acumulador_soma = 0
for n in range(menor, maior):
    if n % 2 != 0:
        acumulador_soma += n
print(abs(acumulador_soma))
