# -*- coding: utf-8 -*-

while True:
    tecla_defeituosa, numero_digitado = input().split()
    
    if tecla_defeituosa == '0' and numero_digitado == '0':
        break

    valor_impresso = []
    for numero in numero_digitado:
        if numero == tecla_defeituosa:
            pass
        else:
            valor_impresso.append(numero)

    numero_impresso = None
    if len(valor_impresso):
        numero_impresso = int(''.join(valor_impresso))
    else:
        numero_impresso = 0

    print(numero_impresso)

# 00 : 17 : 58
