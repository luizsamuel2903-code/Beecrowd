# -*- coding: utf-8 -*-

ordem_leitura = list(map(int, input().split()))
ordem_crecente = sorted(ordem_leitura)

for i in range(3): print(ordem_crecente[i])
print()
for i in range(3): print(ordem_leitura[i])

# 00: 10: 42
