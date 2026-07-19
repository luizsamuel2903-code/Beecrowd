# -*- coding: utf-8 -*-

a, n = map(int, input().split())

soma = 0
for i in range(0, n):
    soma += i
print(soma)