# -*- coding: utf-8 -*-

command = input()
matriz = [[0 for _ in range(12)] for _ in range(12)]

number_of_elements = 0
accumulator_of_values = 0
for row in range(12):
    for column in range(12):
        value = float(input())
        if column > row and column < (11-row):
            number_of_elements += 1
            accumulator_of_values += value
if command == 'S': print(f'{accumulator_of_values:.1f}')
if command == 'M': print(f'{accumulator_of_values/number_of_elements:.1f}')
