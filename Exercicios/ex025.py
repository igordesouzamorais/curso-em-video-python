#025 Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome.
nome = str(input('Digite seu nome: ')).strip()

if nome.upper().count('SILVA') > 0:
    print('Voce tem Silva no nome')
else:
    print('Voce nao tem Silva no nome')

# opcao do exercicio
# print('SILVA' in nome.upper())
