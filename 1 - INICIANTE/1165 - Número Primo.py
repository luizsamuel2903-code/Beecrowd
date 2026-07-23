# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n = int(input())
    d = []
    for i in range(1, n+1):
        if n % i == 0:
            d.append(i)
    if len(d) == 2:
        print(f'{n} eh primo')
    else:
        print(f'{n} nao eh primo')
