# -*- coding: utf-8 -*-

while True:
    x = int(input())
    if x == 0: break

    if x % 2 != 0: x += 1
    
    s = 0
    for i in range(x, x + 10, 2):
        s += i
    print(s)