# -*- coding: utf-8 -*-

COMISSAO = 15

nome_vendedor, salario_fixo, total_vendas = input(), float(input()), float(input())
salario_total = salario_fixo + (COMISSAO / 100 * total_vendas)

print(f'TOTAL = R$ {salario_total:.2f}')
