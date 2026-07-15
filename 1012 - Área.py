# -*- coding: utf-8 -*-

PI = 3.14159

A, B, C = map(float, input().split())

FORMULAS = {
    'TRIANGULO': lambda a, b, c: (a * c) / 2,
    'CIRCULO'  : lambda a, b, c: PI * (c ** 2),
    'TRAPEZIO' : lambda a, b, c: ((a + b) * c) / 2,
    'QUADRADO' : lambda a, b, c: b ** 2,
    'RETANGULO': lambda a, b, c: a * b 
}

for nome, formula in FORMULAS.items():
    print(f'{nome}: {formula(A, B, C):.3f}')
