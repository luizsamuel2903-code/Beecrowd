# -*- coding: utf-8 -*-

alcool = gasolina = diesel = 0

continua = True
while continua:
    entrada = int(input())
    if entrada == 1: alcool += 1
    elif entrada == 2: gasolina += 1
    elif entrada == 3: diesel += 1
    elif entrada == 4: break
print(f'''MUITO OBRIGADO
Alcool: {alcool}
Gasolina: {gasolina}
Diesel: {diesel}''')

# 00 : 05 : 08, 38
