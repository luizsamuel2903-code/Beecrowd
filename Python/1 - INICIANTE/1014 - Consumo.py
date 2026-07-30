# -*- coding: utf-8 -*-

'''
distancia_percorrida, combustivel_gasto = [float(input()) for _ in range(2)]
total_consumo = distancia_percorrida / combustivel_gasto 

print(f'{total_consumo:.3f} km/l')
'''

(lambda a, b: print(f'{a / b:.3f} km/l')) (float(input()), float(input()))