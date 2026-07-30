# -*- coding: utf-8 -*-

vetor_original = [int(input()) for _ in range(10)]
novo_vetor = [1 if i <= 0 else i for i in vetor_original]

for i, v in enumerate(novo_vetor):
    print(f'X[{i}] = {v}')
    