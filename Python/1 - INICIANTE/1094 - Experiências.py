# -*- coding: utf-8 -*-

casos = int(input())

sapos = ratos = coelhos = 0 
for i in range(casos):
    quantidade, tipo = input().split()
    quantidade = int(quantidade)    
    if tipo == 'C': coelhos += quantidade
    elif tipo == 'S': sapos += quantidade
    elif tipo == 'R': ratos += quantidade

total_cobaias = sapos + coelhos + ratos
percentual_sapos = (sapos / total_cobaias) * 100
percentual_ratos = (ratos / total_cobaias) * 100
percentual_coelhos = (coelhos / total_cobaias) * 100

print(f'''Total: {total_cobaias} cobaias
Total de coelhos: {coelhos}
Total de ratos: {ratos}
Total de sapos: {sapos}
Percentual de coelhos: {percentual_coelhos:.2f} %
Percentual de ratos: {percentual_ratos:.2f} %
Percentual de sapos: {percentual_sapos:.2f} %''')

# 00 : 14 : 04, 32
