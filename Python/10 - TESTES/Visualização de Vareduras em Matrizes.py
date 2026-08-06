dm = 12
m = [['[ ]' for _ in range(dm)] for _ in range(dm)]

for i in range(dm):
    for j in range(dm):
        if i+j>11 and j<6: m[i][j] = '\033[32m[ ]\033[m'
        if i-j>=1 and j>5: m[i][j] = '\033[34m[ ]\033[m'
for i in m: print(''.join(i))
