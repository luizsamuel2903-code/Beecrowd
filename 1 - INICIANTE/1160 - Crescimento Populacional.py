# -*- coding: utf-8 -*-

for _ in range(int(input())):
    pa, pb, g1, g2 = input().split()
    pa, pb = map(int, [pa, pb])
    g1, g2 = map(float, [g1, g2])
    
    anos = 0
    while pa <= pb:
        pa *= g1
        pb *= g2
        anos += 1