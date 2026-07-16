# -*- coding: utf-8 -*-

ddd_destino = {
    61: 'Brasilia',
    71: 'Salvador',
    11: 'Sao Paulo',
    21: 'Rio de Janeiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Vitoria',
    31: 'Belo Horizonte'
}

ddd = int(input())
if ddd in ddd_destino.keys():
    destino = ddd_destino[ddd]
    print(destino)
else:
    print('DDD nao cadastrado')

# 00 : 07 : 39
