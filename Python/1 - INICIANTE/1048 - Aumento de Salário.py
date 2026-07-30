# -*- coding: utf-8 -*-

salario = float(input())
percentual = None

if 0 <= salario <= 400: percentual = 0.15
elif 400.1 <= salario <= 800: percentual = 0.12
elif 800 <= salario <= 1200: percentual = 0.1
elif 1200.1 <= salario <= 2000: percentual = 0.07
elif salario > 2000: percentual = 0.04

salario_reajustado = salario + (salario * percentual)
reajuste_ganho = salario_reajustado - salario

print(f'''Novo salario: {salario_reajustado:.2f}
Reajuste ganho: {reajuste_ganho:.2f}
Em percentual: {int(percentual * 100)} %''')

# 00 : 09 : 42
