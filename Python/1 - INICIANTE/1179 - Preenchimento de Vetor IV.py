# -*- coding: utf-8 -*-

impar = []
par = []
for i in range(15):
    numero = int(input())
    if numero % 2 == 0:
        if len(par) >= 5:
            for i, v in enumerate(par):
                print(f'par[{i}] = {v}')
            par.clear()
        par.append(numero)
    else:
        if len(impar) >= 5:
            for i, v in enumerate(impar):
                print(f'impar[{i}] = {v}')
            impar.clear()
        impar.append(numero)
        
for i, v in enumerate(impar):
    print(f'impar[{i}] = {v}')
for i, v in enumerate(par):
    print(f'par[{i}] = {v}')