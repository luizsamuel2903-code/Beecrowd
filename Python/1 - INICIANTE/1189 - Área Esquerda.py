# -*- coding: utf-8 -*-

c, a, e = input(), 0, 0

for linha in range(12):
    for coluna in range(12):
        v = float(input())
        if coluna < linha and coluna < 11 - linha:
            a += v
            e += 1

if c == 'S': print(f'{a:.1f}')
elif c == 'M': print(f'{a/e:.1f}')