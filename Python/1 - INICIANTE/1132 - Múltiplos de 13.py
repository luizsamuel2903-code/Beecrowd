# -*- coding: utf-8 -*-

x_y = [int(input()) for i in range(2)]
menor, maior = sorted(x_y)

soma = 0
for i in range(menor, maior+1):
    if i % 13 != 0: soma += i
print(soma) 

# 00 : 07 : 05, 48
