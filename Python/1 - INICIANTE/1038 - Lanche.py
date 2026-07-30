# -*- coding: utf-8 -*-

VALORES = [4.00, 4.50, 5.00, 2.00, 1.50]

codigo, quantidade = map(int, input().split())

valor_unitario = VALORES[codigo-1]
valor_total = valor_unitario * quantidade

print(f'Total: R$ {valor_total:.2f}')

# 00: 05: 44
