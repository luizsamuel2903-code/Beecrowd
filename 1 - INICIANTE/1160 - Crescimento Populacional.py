# -*- coding: utf-8 -*-

for _ in range(int(input())):
    pa, pb, g1, g2 = input().split()
    pa, pb = map(int, [pa, pb])
    g1, g2 = map(float, [g1, g2])
    
    anos = 0
    while pa <= pb and anos <= 100:
        pa = int(pa*(g1/100))
        pb = int(pb*(g2/100))
        anos += 1
    if anos > 100: print('Mais de 1 seculo')
    else: print(f'{anos} anos.')