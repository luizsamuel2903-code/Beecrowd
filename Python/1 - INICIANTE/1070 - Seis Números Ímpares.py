# -*- coding: utf-8 -*-

numero = int(input())
if numero % 2 != 0:
    for n in range(6):
        print(numero + n*2)
else:
    numero += 1
    for n in range(6):
        print(numero + n*2)

# 00 : 03 : 58,08
