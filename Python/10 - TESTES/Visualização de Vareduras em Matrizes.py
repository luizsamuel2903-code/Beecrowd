dm = 10
m = [['[ ]' for _ in range(dm)] for _ in range(dm)]

for i in range(dm):
    for j in range(dm):
        # Insira a logica de varetura da matriz
        if i > j: 
            m[i][j] = '\033[32m[ ]\033[m'

    # Impresao completa da matriz
    for i in m: print(''.join(i))
    else: print()

