salario = float(input())

if salario <= 2000.00:
    print('Isento')
else:
    imposto = 0.0
    if salario > 4500.00:
        imposto += (salario - 4500.00) * 0.28
        salario = 4500
    if salario > 3000:
        imposto += (salario - 3000) * 0.18
        salario = 3000
    if salario > 2000:
        imposto += (salario - 2000) * 0.08
        
    print(f'R$ {imposto:.2f}')

# 00 : 08 : 08
