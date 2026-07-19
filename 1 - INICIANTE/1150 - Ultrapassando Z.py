# -*- coding: utf-8 -*-

x = z = int(input())

while z <= x:
    z = int(input())

a = []
for i in range(x, z):
    a.append(i)
    if sum(a) >= z: break
print(len(a))

# 00 : 09 : 03, 24
