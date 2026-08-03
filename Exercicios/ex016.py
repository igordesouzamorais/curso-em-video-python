# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Ex:
# Digite um número: 6.127
# 0 número 6.127 tem o Inteira 6.

import math

real = float(input('Digite um numero Real: '))
print('Sua porcao inteira é: {}'.format(math.floor(real)))
print('Sua porcao inteira é: {}'.format(math.trunc(real)))
print('Sua porcao inteira é: {}'.format(int(real)))
