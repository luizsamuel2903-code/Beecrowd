# -*- coding: utf-8 -*-

c, a, e = input(), 0, 0

for i in range(12):
    for j in range(12):
        v = float(input())
        if i+j>11 and i<6 or i<j and 5<i:
            a += v
            e += 1
            
if c == 'S': print(f'{a:.1f}')
if c == 'M': print(f'{a/e:.1f}')