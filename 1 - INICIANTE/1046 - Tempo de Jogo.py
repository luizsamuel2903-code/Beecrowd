# -*- coding: utf-8 -*-

inicio, final = map(int, input().split())
tempo = None

if inicio > final:
    tempo = abs((inicio - final) - 24)
elif final > inicio: 
    tempo = final - inicio
elif inicio == final:
    tempo = 24

print(f'O JOGO DUROU {tempo} HORA(S)')

# 00: 06: 12

'''
inicio, final = map(int, input().split())

if final <= inicio:
    tempo = (final + 24) - inicio
else:
    tempo = final - inicio

print(f"O JOGO DUROU {tempo} HORA(S)")
'''