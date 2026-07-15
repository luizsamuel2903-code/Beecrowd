# -*- coding: utf-8 -*-

FORMULA_MAIOR = lambda a, b: (a + b + abs(a - b)) / 2

a, b, c = map(int, input().split())
maior = FORMULA_MAIOR(FORMULA_MAIOR(a, b), c)

print(f'{int(maior)} eh o maior')
