# -*- coding: utf-8 -*-

valores = list(map(int, input().split()))
a = valores[0]

index = 1
while valores[index] <= 0:
    index += 1

n = valores[index]

soma = 0
for i in range(0, n):
    soma += a + i
print(soma)


# 18