# -*- coding: utf-8 -*-

while True:
    x = int(input())
    if x % 2 != 0: x += 2
    
    s = 0
    for i in range(x, x + 11, 2):
        s += x
    print(s)