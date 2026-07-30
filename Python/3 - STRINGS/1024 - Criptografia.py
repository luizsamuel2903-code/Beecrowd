# -*- coding: utf-8 -*-

quantidade_linhas = int(input())

linhas_descri = []
for _ in range(quantidade_linhas):
    linhas_descri.append(input())

linhas_codificadas = []
for linha in linhas_descri:
    novas_letras = []
    for letra in linha:
        nova_letra = letra
        if letra.isalpha():
            nova_letra = chr(ord(letra) +3)
        novas_letras.append(nova_letra)    
    linhas_codificadas.append(''.join(novas_letras))

linhas_invertidas = []
for linha in linhas_codificadas:
    linha_invertida = linha[::-1]
    linhas_invertidas.append(linha_invertida)

linhas_truncadas = []
for linha in linhas_invertidas:
    novas_letras = []
    for index, letra in enumerate(linha):
        nova_letra = letra
        if index >= len(linha) // 2:
            nova_letra = chr(ord(letra) -1)
        novas_letras.append(nova_letra)
    linhas_truncadas.append(''.join(novas_letras))

for linha in linhas_truncadas: 
    print(linha)

# 00: 59 : 24