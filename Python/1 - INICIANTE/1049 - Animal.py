# -*- coding: utf-8 -*-

palavra1, palavra2, palavra3 = [input() for _ in range(3)]
animal = None

if palavra1 == 'vertebrado':
    if palavra2 == 'ave':
        if palavra3 == 'carnivoro':
            animal = 'aguia'
        else:
            animal = 'pomba'
    
    else:
        if palavra3 == 'onivoro':
            animal = 'homem'
        else:
            animal = 'vaca'

else:
    if palavra2 == 'inseto':
        if palavra3 == 'hematofago':
            animal = 'pulga'
        else:
            animal = 'lagarta'

    else:
        if palavra3 == 'hematofago':
            animal = 'sanguessuga'
        else:
            animal = 'minhoca'

print(animal)

# 00 : 11 : 26
