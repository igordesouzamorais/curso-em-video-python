valor = int(input('Digite a tabuada desejada: '))

print('Tabuada do {}:'.format(valor))
print('-' * 12)
for i in range(1, 11):
    print('{} * {:2} = {}'.format(valor, i, i*valor))
print('-' * 12)