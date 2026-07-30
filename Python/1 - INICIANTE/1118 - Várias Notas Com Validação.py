notas = []
fechar_programa = False

while not fechar_programa:
    nota = float(input())
    if 0 <= nota <= 10: notas.append(nota)
    else: print('nota invalida')

    if len(notas) == 2: 
        print(f'media = {sum(notas) / 2:.2f}')

        while True:
            print('novo calculo (1-sim 2-nao)')
            novo_calculo = int(input())
            
            if novo_calculo == 1:
                notas = []
                break
            elif novo_calculo == 2:
                fechar_programa = True
                break

# 00 : 15 : 59, 17    
