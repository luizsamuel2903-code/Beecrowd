# -*- coding: utf-8 -*-

t = int(input())

n = []
for i in range(1000):
    v = i % t
    n.append(v)
    print(f'N[{i}] = {v}')
    