#023 Fasa um programa que leia um numero de 0 a 9999 e mostre na tela
# cada um dos digitos separados.

# Ex:
# Digite um número: 1834
# unidada: 4
# dezena: 3
# centena: 8
# milhar: 1

# numero = str(input('Digite um numero entre 0 e 9999: '))
#
# if (len(numero) == 1):
#     print('unidade', numero[0])
# if(len(numero) == 2):
#     print('dezena ', numero[0])
#     print('unidade ', numero[1])
# if (len(numero) == 3):
#     print('centena ', numero[0])
#     print('dezena ', numero[1])
#     print('unidade ', numero[2])
# if (len(numero) == 4):
#     print('milhar ', numero[0])
#     print('centena ', numero[1])
#     print('dezena ', numero[2])
#     print('unidade ', numero[3])

# solucao com inteiros
numero_inteiro = int(input('Digite um numero inteiro de 0 a 9999: '))
print('unidade: {}'.format(numero_inteiro // 1 % 10))
print('dezena: {}'.format(numero_inteiro // 10 % 10))
print('centena: {}'.format(numero_inteiro // 100 % 10))
print('milhar: {}'.format(numero_inteiro // 1000 % 10))
