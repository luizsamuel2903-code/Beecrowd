# -*- coding: utf-8 -*-

s = 0
denominador = 1
for numerador in range(1, 39+1, 2):
    s += numerador / denominador
    denominador *= 2
print(f'{s:.2f}')

# 00 : 08 : 37, 95
