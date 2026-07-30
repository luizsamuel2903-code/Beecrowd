# -*- coding: utf-8 -*-

x_y = [int(input()) for _ in range(2)]
menor, maior = sorted(x_y)

for i in range(menor+1, maior):
    if i % 5 == 2 or i % 5 == 3:
        print(i)

# 00 : 02 : 48, 27
