# Faca um programa que leia uma frase pelo teclado e mostre:
# Quantas vezas aparece a letra "A".
# Em que posisao ela aparece a primeira vez.
# Em que posisao ela aparece a última vez.
frase = input('Digite uma frase: ')
print('Quantidade de letra A: {}'.format(frase.upper().count('A')))
print('O A aparece a primeiro vez na posição: {}'.format(frase.upper().find('A')))

for indice,letra in enumerate(frase.upper()):
    if letra == 'A':
        posicao = indice

print('O A aparece pela ultima vez na posição: {}'.format(posicao))
