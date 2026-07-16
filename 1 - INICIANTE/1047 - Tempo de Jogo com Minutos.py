# -*- coding: utf-8 -*-

hor_ini, min_ini, hor_fin, min_fin = map(int, input().split())
inter_ini = hor_ini*60 + min_ini
inter_fin = hor_fin*60 + min_fin

inter = None

if inter_ini > inter_fin: 
    inter = (inter_fin + 1440) - inter_ini
elif inter_fin > inter_ini: 
    inter = inter_fin - inter_ini
elif inter_ini == inter_fin: 
    inter = 1440

inter_hor = inter // 60
inter_min = inter % 60

print(f'O JOGO DUROU {inter_hor} HORA(S) E {inter_min} MINUTO(S)')

# 00: 25: 15
