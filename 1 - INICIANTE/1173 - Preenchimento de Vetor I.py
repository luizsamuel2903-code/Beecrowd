# -*- coding: utf-8 -*-

valor = int(input())
vetor_modificado = [valor]
for i in range(1, 10):
    if len(vetor_modificado) == 1:
        vetor_modificado.append(valor*2)
    else:
        ultimo_valor = vetor_modificado[-1]
        vetor_modificado.append(ultimo_valor*2)

for i, v in enumerate(vetor_modificado):
    print(f'N[{i}] = {v}')
