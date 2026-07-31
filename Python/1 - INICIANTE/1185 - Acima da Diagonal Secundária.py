# -*- coding: utf-8 -*-

matriz = [[0 for _ in range(12)] for _ in range(12)]

command = input()

accumulator_of_values = 0
number_of_elements = 0
for row in range(12):
    for column in range(12):
        number = float(input())
        if column + row < 11:
            accumulator_of_values += number
            number_of_elements += 1

if command == 'S': print(f'{accumulator_of_values:.1f}')
if command == 'M': print(f'{accumulator_of_values/number_of_elements:.1f}')

