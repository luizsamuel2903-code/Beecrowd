# -*- coding: utf-8 -*-

numeros = [int(input()) for _ in range(5)]

pares = impares = positivos = negativos = 0
for n in numeros:
    if n % 2 == 0: pares += 1
    else: impares += 1
    
    if n > 0: positivos += 1
    else: 
        if n != 0: negativos += 1

print(f'''{pares} valor(es) par(es)
{impares} valor(es) impar(es)
{positivos} valor(es) positivo(s)
{negativos} valor(es) negativo(s)''')

# 00 : 07 : 52
