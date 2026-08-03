# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de triângulo retângulo
# calcule e mostre o comprimento da hipotenusa.

from math import sqrt, hypot

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))

soma_catetos = (cateto_oposto**2) + (cateto_adjacente**2)
hipotenusa = sqrt(soma_catetos)

hi = hypot(cateto_oposto, cateto_adjacente)

print('Comprimento da hipotenusa é: {:.2f}'.format(hipotenusa))
print('Comprimento da hipotenusa é: {:.2f}'.format(hi))
