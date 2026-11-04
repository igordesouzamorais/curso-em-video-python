#025 Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome.
nome = input('Digite seu nome: ')
if nome.upper().count('SILVA') > 0:
    print('Voce tem SILVA no nome')
else:
    print('Voce nao tem SILVA no nome')
