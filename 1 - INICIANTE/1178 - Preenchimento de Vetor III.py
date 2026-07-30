# -*- coding: utf-8 -*-

x = float(input())
v = [x]

print(f'N[0] = {v[0]:.4f}')
for i in range(1, 100):
    m = v[-1] / 2
    v.append(m)
    print(f'N[{i}] = {m:.4f}')
