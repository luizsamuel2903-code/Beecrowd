# -*- coding: utf-8 -*-

dias = int(input())

anos, dias = divmod(dias , 365)
meses, dias = divmod(dias, 30)

print(f'{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)')
