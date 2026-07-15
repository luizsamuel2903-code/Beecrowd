# -*- coding: utf-8 -*-

n = int(input())

for _ in range(n):
    ele = input().split()
    ope = ele[3]
    n1 = int(ele[0])
    d1 = int(ele[2])
    n2 = int(ele[4])
    d2 = int(ele[6])

    num = den = None
    if ope == '+':
        num = (n1*d2 + n2*d1)
        den = (d1*d2)
    if ope == '-':
        num = (n1*d2 - n2*d1)
        den = (d1*d2)
    if ope == '*':
        num = (n1*n2)
        den = (d1*d2)
    if ope == '/':
        num = (n1*d2)
        den = (n2*d1)

    a = num
    b = den
    while b:
        a, b = b, a % b
    mdc = abs(a)

    num_sim = num // mdc
    den_sim = den // mdc 

    print(f'{num}/{den} = {num_sim}/{den_sim}')

# 2: 57: 12
