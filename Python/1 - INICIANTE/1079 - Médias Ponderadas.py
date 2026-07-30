# -*- coding: utf-8 -*-

n = int(input())
for i in range(n):
    a, b, c = map(float, input().split())
    media = (a*2 + b*3 + c*5) / 10
    print(round(media, 1))

# 00 : 03 : 50, 52
