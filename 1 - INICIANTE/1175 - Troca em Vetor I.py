# -*- coding: utf-8 -*-

vetor = [int(input()) for _ in range(20)]
vetor.reverse()
for i, v in enumerate(vetor):
    print(f'N[{i}] = {v}')
