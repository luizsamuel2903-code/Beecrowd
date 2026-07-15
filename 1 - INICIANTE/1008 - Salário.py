# -*- coding: utf-8 -*-

number, hours_worked, hourly_wage = int(input()), int(input()), float(input())
salary = hours_worked * hourly_wage

print('NUMBER =', number)
print(f'SALARY = U$ {salary:.2f}')
