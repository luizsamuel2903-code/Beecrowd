# -*- coding: utf-8 -*-

segundos = int(input())

horas, resto = divmod(segundos, 3600)
minutos, segundos_restantes = divmod(resto, 60)

print(f'{horas}:{minutos}:{segundos_restantes}')

'''
segundos = int(input())

horas = segundos // 3600; segundos %= 3600
minutos = segundos // 60  ; segundos %= 60

print(f'{horas}:{minutos}:{segundos}')
'''
