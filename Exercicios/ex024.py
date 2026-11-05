#024 Crie um programa que leia o nome de uma pessoa e diga se ela começa ou não com o nome SANTO
cidade = input('Em que cidade voce nasceu: ')

if cidade.strip().upper().startswith('SANTO'):
    print('Você nasceu em uma cidade que começa com Santo')
else:
    print('Você não nasceu em uma cidade que começa com Santo')