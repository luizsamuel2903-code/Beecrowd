# -*- coding: utf-8 -*-

notas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

valor = float(input())
valor = round(valor * 100)

print('NOTAS:')
for nota in notas:
    quantidade, valor = divmod(valor, nota * 100)
    print(f'{quantidade} nota(s) de R$ {nota:.2f}')

print('MOEDAS:')
for moeda in moedas:
    quantidade, valor = divmod(valor, round(moeda * 100))
    print(f"{quantidade} moeda(s) de R$ {moeda:.2f}")

""" 
valor = float(input())

notas_100, resto = divmod(valor, 100)
notas_50, resto = divmod(resto, 50)
notas_20, resto = divmod(resto, 20)
notas_10, resto = divmod(resto, 10)
notas_5, resto = divmod(resto, 5)
notas_2, resto = divmod(resto, 2)

moedas_1, resto = divmod(resto, 1.00)
moedas_50, resto = divmod(resto, 0.50)
moedas_25, resto = divmod(resto, 0.25)
moedas_10, resto = divmod(resto, 0.10)
moedas_05, resto = divmod(resto, 0.05)
moedas_01, resto = divmod(resto, 0.01)

print(f'''NOTAS:
{int(notas_100)} nota(s) de R$ 100.00
{int(notas_50)} nota(s) de R$ 50.00
{int(notas_20)} nota(s) de R$ 20.00
{int(notas_10)} nota(s) de R$ 10.00
{int(notas_5)} nota(s) de R$ 5.00
{int(notas_2)} nota(s) de R$ 2.00
MOEDAS:
{int(moedas_1)} moeda(s) de R$ 1.00
{int(moedas_50)} moeda(s) de R$ 0.50
{int(moedas_25)} moeda(s) de R$ 0.25
{int(moedas_10)} moeda(s) de R$ 0.10
{int(moedas_05)} moeda(s) de R$ 0.05
{int(moedas_01)} moeda(s) de R$ 0.01''')
"""