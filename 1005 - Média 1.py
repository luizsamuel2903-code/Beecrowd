# -*- coding: utf-8 -*-

PESO_A = 3.5
PESO_B = 7.5
VALOR_MAXIMO = 10.0

a = float(input())
b = float(input())

media = ((a * PESO_A) + (b * PESO_B)) / 11.0

media_limitada = min(VALOR_MAXIMO, media)

print(f'MEDIA = {media_limitada:.5f}')
