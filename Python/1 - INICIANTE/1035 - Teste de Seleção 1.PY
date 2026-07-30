# -*- coding: utf-8 -*-

A, B, C, D = map(int, input().split())

valores_aceitos = False

if B > C and D > A:
    if C + D > A + B:
        if C > 0 and D > 0:
            if A % 2 == 0:
                valores_aceitos = True
if valores_aceitos: print('Valores aceitos') 
else: print('Valores nao aceitos')  

# 00: 11: 39
