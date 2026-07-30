# -*- coding: utf:8 -*-

DISTANCIA = lambda x1, y1, x2, y2: ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
pontos = [float(i) for _ in range(2) for i in input().split()]

print(f'{DISTANCIA(*pontos):.4f}')

# (lambda p1, p2: print(f'{((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5:.4f}')) (*[[float(i) for i in input().split()] for _ in range(2)])
