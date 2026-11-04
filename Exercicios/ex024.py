#024 Crie um programa que leia o nome de uma pessoa e diga se ela começa ou não com o nome SANTO
nome = input('Digite o nome: ')

if nome.upper().startswith('SANTO'):
    print('O nome {} começa com SANTO'.format(nome))
else:
    print('O nome {} não começa com SANTO'.format(nome))