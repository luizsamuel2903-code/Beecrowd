# -*- coding: utf-8 -*-

VALOR_MAXIMO = 10
PESO_A, PESO_B, PESO_C = 2, 3, 5

A, B, C = [float(input()) for _ in range(3)]

media = ((A * PESO_A) + (B * PESO_B) + (C * PESO_C)) / 10.0
media_limitada = min(VALOR_MAXIMO, media)

print(f'MEDIA = {media_limitada:.1f}')
