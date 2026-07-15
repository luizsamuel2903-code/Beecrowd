# -*- coding: utf-8 -*- 

n1, n2, n3, n4 = map(float, input().split())

media = (n1*2 + n2*3 + n3*4 + n4) / 10 
print(f'Media: {media:.1f}')

if media >= 7: print('Aluno aprovado.')
elif media < 5: print('Aluno reprovado.')
elif 5 <= media <= 6.9:
    print('Aluno em exame.')
    nota_exame = float(input())

    print(f'Nota do exame: {nota_exame}')
    nova_media = (nota_exame + media) / 2

    if nova_media >= 5: print('Aluno aprovado.')
    elif nova_media < 5: print('Aluno reprovado.')

    print(f'Media final: {nova_media}')

# 00: 13: 55
