# -*- coding: utf-8 -*-

CONSUMO_KM_L = 12

tempo_de_viagem, velocidade_media = int(input()), int(input())

distancia_percorrida = velocidade_media * tempo_de_viagem
consumo_total = distancia_percorrida / CONSUMO_KM_L

print(f'{consumo_total:.3f}')
