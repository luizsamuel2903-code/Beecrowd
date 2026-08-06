dm = 12
m = [['[ ]' for _ in range(dm)] for _ in range(dm)]

for i in range(dm):
    for j in range(dm):
        #if : m[i][j] = '\033[34m[ ]\033[m'
        #if i<j and 5<i : m[i][j] = '\033[32m[ ]\033[m'
        ...

for i in m: print(''.join(i))
