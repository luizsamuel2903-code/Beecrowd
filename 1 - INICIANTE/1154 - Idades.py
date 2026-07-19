# -*- coding: utf-8 -*-

idades = []
while True:
    idade = int(input())
    if idade < 0: break
    else: idades.append(idade)
print(sum(idades) / len(idades))
