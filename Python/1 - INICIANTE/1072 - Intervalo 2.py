# -*- coding: utf-8 -*-

n = int(input())

n_in =  n_out = 0
for i in range(n):
    x = int(input())
    if 10 <= x <= 20: n_in += 1
    else: n_out += 1
else:
    print(f'{n_in} in\n{n_out} out')
