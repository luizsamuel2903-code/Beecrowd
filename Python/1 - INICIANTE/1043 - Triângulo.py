# -*- coding: utf-8 -*-

a, b, c = list(map(float, input().split()))
maior = max(a, b, c)

if maior < abs(a + b + c - maior):
    perimetro = a + b + c
    print(f'Perimetro = {perimetro:.1f}')

else:
    area = ((a + b) * c) / 2
    print(f'Area = {area:.1f}')

# 00: 10: 30

