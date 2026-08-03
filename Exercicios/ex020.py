# O mesmo professor do desafio anterior quer sortear a ordem de apresentasao de trabalhos dos alunos.
# Fasa um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alunos = []

for i in range(1,5):
    aluno = input('Digite o nome do aluno: ')
    alunos.append(aluno)

random.shuffle(alunos)

print('Ordem de apresentação será: ')

for i in range(4):
    print('{}º aluno: {}'.format(i+1,alunos[i]))
