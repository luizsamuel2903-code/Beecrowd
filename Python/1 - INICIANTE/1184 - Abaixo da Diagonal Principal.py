# -*- coding: utf-8 -*-

dm = 12
matriz = [[0 for _ in range(dm)] for _ in range(dm)]
command = input()

accumulator_of_value = 0
number_of_elements = 0
for row in range(dm):
    for column in range(dm):
        matriz[row][column] = float(input())
        if row > column:
            accumulator_of_value += matriz[row][column]
            number_of_elements += 1
if command == 'S': print(f'{accumulator_of_value:.1f}')
if command == 'M': print(f'{accumulator_of_value/number_of_elements:.1f}')

