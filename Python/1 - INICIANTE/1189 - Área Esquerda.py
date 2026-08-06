# -*- coding: utf-8 -*-

c, a, e = input(), 0, 0

for i in range(12):
    for j in range(12):
        v = float(input())
        if j<i and j<11-i:
            a += v
            e += 1

if c == 'S': print(f'{a:.1f}')
elif c == 'M': print(f'{a/e:.1f}')