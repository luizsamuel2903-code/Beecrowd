# -*- coding: utf-8 -*-

idades = []
while True:
    idade = float(input())
    if idade < 0: break
    else: idades.append(idade)
media = sum(idades) / len(idades)
print(f'{media:.2f}')

# 00 : 08 : 12, 31
