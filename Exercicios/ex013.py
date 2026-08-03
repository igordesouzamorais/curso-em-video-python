salario = float(input('Digite o salario: '))
aumento = float(input('Digite o percentual de aumento: '))

# novo = salario + (salario * aumento / 100)
novo = salario * (aumento / 100 + 1)

print('O seu salario com {}% de aumento é: {:.2f}'.format(aumento, novo))
