# -*- coding: utf-8 -*-

# Formula da VELOCIDADE RELATIVA: Vrel = Vy - Vx
# Formula do TEMPO (para horas): Th = Distancia / Vrel

VELOCIDADE_CARRO_X = 60
VELOCIDADE_CARRO_Y = 90

distancia_entre_carros = int(input())

velocidade_relativa = abs(VELOCIDADE_CARRO_X - VELOCIDADE_CARRO_Y)
tempo_em_horas = distancia_entre_carros / velocidade_relativa
tempo_em_minutos = tempo_em_horas * 60

print(int(tempo_em_minutos), 'minutos')
