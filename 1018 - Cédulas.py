# -*- coding: utf-8 -*-

numero = int(input())
valor = numero

n100 = valor // 100; valor %= 100
n50  = valor // 50;  valor %= 50
n20  = valor // 20;  valor %= 20
n10  = valor // 10;  valor %= 10
n5   = valor // 5;   valor %= 5
n2   = valor // 2;   valor %= 2
n1   = valor // 1;   valor %= 1

print(f'''{numero}
{n100} nota(s) de R$ 100,00
{n50} nota(s) de R$ 50,00
{n20} nota(s) de R$ 20,00
{n10} nota(s) de R$ 10,00
{n5} nota(s) de R$ 5,00
{n2} nota(s) de R$ 2,00
{n1} nota(s) de R$ 1,00''')

""" LOOP DE SUBTRACOES
_100 = _50 = _20 = _10 = _5 = _2 = _1 = 0

numero_de_entrada = int(input())
numero = numero_de_entrada

while numero >= 0:
    if   numero >= 100: numero -= 100; _100 += 1
    elif numero >= 50 : numero -= 50 ; _50  += 1
    elif numero >= 20 : numero -= 20 ; _20  += 1
    elif numero >= 10 : numero -= 10 ; _10  += 1
    elif numero >= 5  : numero -= 5  ; _5   += 1
    elif numero >= 2  : numero -= 2  ; _2   += 1
    if   numero <= 0  : break

print(f'''{numero}
{_100} nota(s) de R$ 100,00
{_50} nota(s) de R$ 50,00
{_20} nota(s) de R$ 20,00
{_10} nota(s) de R$ 10,00
{_5} nota(s) de R$ 5,00
{_2} nota(s) de R$ 2,00
{_1} nota(s) de R$ 1,00''')
"""
