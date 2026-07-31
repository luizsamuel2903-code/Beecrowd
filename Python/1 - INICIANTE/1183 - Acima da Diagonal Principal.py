# -*- coding: utf-8 -*-

dm = 12
matriz = [[0 for _ in range(dm)] for _ in range(dm)]
command = input()

accumulator = 0
number_of_elements = 0
for row in range(dm):
    for column in range(dm):
        value = float(input())
        if column > row:
            accumulator += value
            number_of_elements += 1

if command == 'S': print(f'{accumulator:.1f}')
if command == 'M': print(f'{accumulator/number_of_elements:.1f}')
        