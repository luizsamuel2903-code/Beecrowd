# -*- coding: utf-8 -*-


while True:
    entrada = map(int, input().split())
    menor, maior = sorted(entrada)
    
    if maior <= 0 or menor <= 0:
        break

    soma = 0
    for i in range(menor, maior+1):
        print(i, end=' ')
        soma += i
    print(f'Sum={soma}')

# 00 : 08 : 39, 50
