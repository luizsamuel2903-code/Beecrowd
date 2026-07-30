# -*- coding utf-8 -*-

vitorias_inter = vitorias_gremio = empates =0
total_grenais = 0

while True:
    gols_inter, gols_gremio = map(int, input().split())
    if gols_inter == gols_gremio: empates += 1
    elif gols_inter > gols_gremio : vitorias_inter += 1
    else: vitorias_gremio += 1
    total_grenais += 1

    print('Novo grenal (1-sim 2-nao)')
    novo_grenal = int(input())
    if novo_grenal == 2: break

mais_venceu = 'Inter' if vitorias_inter > vitorias_gremio else 'Gremio'

print(f'''{total_grenais} grenais
Inter:{vitorias_inter}
Gremio:{vitorias_gremio}
Empates:{empates}
{mais_venceu} venceu mais''')
    
# 00 : 13 : 10, 74