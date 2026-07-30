# -*- coding: utf-8 -*-

for _ in range(int(input())):
    a, b, c = 1, 1, 0
    
    n_esimo = int(input())
    for _ in range(n_esimo):
        c = a
        a, b = b, a+b
    print(f'Fib({n_esimo}) = {c}')

