# -*- coding: utf-8 -*-

a, n = map(int, input().split())

for i in range(0, n-1):
    a += i
print(a)