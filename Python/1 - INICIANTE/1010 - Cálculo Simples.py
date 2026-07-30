# -*- coding: utf-8 -*-

TIPOS = [int, int, float]

codigo_1, numero_1, unitario_1 = [tipo(valor) for tipo, valor in zip(TIPOS, input().split())]
codigo_2, numero_2, unitario_2 = [tipo(valor) for tipo, valor in zip(TIPOS, input().split())]

valor_a_pagar = (numero_1 * unitario_1) + (numero_2 * unitario_2)

print(f'VALOR A PAGAR: R$ {valor_a_pagar:.2f}')
