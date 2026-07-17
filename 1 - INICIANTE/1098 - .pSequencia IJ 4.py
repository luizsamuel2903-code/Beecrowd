# -*- coding: utf-8 -*-

i, j = 0, 0

while i <= 2.1:
    i_arredondado = round(i, 1)
    j_arredondado = round(j, 1)
    
    if float(i_arredondado).is_integer():
        for k in range(1, 4):
            print(f'I={int(i_arredondado)} J={int(j_arredondado + k)}')
    else:
        for k in range(1, 4):
            print(f'I={i_arredondado:.1f} J={j_arredondado + k:.1f}')
            
    i += 0.2
    j += 0.2