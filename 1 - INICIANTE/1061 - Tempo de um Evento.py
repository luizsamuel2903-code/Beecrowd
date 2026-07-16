# -*- coding: utf-8 -*-

dia_ini = int(input()[4:])
hor_ini, min_ini, seg_ini = map(int, input().replace(':', '').split())
dia_fin = int(input()[4:])
hor_fin, min_fin, seg_fin = map(int, input().replace(':', '').split())

total_segundos_inicial = dia_ini*86400 + hor_ini*3600 + min_ini*60 + seg_ini
total_segundos_finais = dia_fin*86400 + hor_fin*3600 + min_fin*60 + seg_fin
 
diferenca_segundos = total_segundos_finais - total_segundos_inicial

duracao_dias, resto_segundos = divmod(diferenca_segundos, 86400)
duracao_horas, resto_segundos = divmod(resto_segundos, 3600)
duracao_minutos, resto_segundos = divmod(resto_segundos, 60)
duracao_segundos = resto_segundos

print(f'''{duracao_dias} dia(s)
{duracao_horas} hora(s)
{duracao_minutos} minuto(s)
{duracao_segundos} segundo(s)''')

# 00 : 24 : 22
