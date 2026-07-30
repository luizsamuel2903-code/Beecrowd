# -*- coding: utf-8 -*-

e = int(input())
for i in range(e):
    n = int(input())
    
    if n == 0:
        print('NULL')
    else: 
        if n % 2 == 0: print('EVEN', end=' ')
        else: print('ODD', end=' ') 

        if n > 0: print('POSITIVE')
        else: print('NEGATIVE')
