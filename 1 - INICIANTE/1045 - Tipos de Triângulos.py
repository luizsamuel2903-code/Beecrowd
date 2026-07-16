# -*- coding: utf-8 -*-

a, b, c = sorted(map(float, input().split()), reverse=True)
conjunto = set([a, b, c])

if a >= b + c: print('NAO FORMA TRIANGULO')
elif a**2 == b**2 + c**2: print('TRIANGULO RETANGULO')
elif a**2 > b**2 + c**2: print('TRIANGULO OBTUSANGULO')
elif a**2 < b**2 + c**2: print('TRIANGULO ACUTANGULO')
if a == b == c: print('TRIANGULO EQUILATERO')
if len(conjunto) == 2: print('TRIANGULO ISOSCELES')

# 00: 17: 27
