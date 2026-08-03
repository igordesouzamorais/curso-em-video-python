# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

from math import sin, cos, tan, radians

angulo = int(input('Digite um angulo: '))
angulo_radianos = radians(angulo)

seno = sin(angulo_radianos)
cosseno = cos(angulo_radianos)
tangente = tan(angulo_radianos)

print('Seno: {:.4f} - Cosseno: {:.4f} - Tangente: {:.4f}'.format(seno, cosseno, tangente))
