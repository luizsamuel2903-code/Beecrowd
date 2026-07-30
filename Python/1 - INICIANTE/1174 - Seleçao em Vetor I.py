# -*- coding: utf-8 -*-

vetor = [float(input())for _ in range(100)]
for i, v in enumerate(vetor):
    if v > 10: pass
    else: print(f'A[{i}] = {v}')
