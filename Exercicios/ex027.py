# Fasa um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamenta.
# Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza
nome = str(input('Digite seu nome: ')).strip()
palavras = nome.split()

print('Primeiro nome: {}, Ultimo nome: {}'.format(palavras[0], palavras[len(palavras)-1]))
