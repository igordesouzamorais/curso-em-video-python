# Faca um programa que leia uma frase pelo teclado e mostre:
# Quantas vezas aparece a letra "A".
# Em que posisao ela aparece a primeira vez.
# Em que posisao ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip()

print('Quantidade de letra A: {}'.format(frase.upper().count('A')))
print('A letra A aparece pela primeira vez na posição: {}'.format(frase.upper().find('A')))

for indice,letra in enumerate(frase.upper()):
    if letra == 'A':
        posicao = indice

print('O A aparece pela ultima vez na posição: {}'.format(posicao))


# opcao do exercicio
# print(frase.upper().find('A'))
# print(frase.upper().rfind('A')) # nao sabia que existia rfind
