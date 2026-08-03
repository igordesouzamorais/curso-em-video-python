# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido.

from random import choice, randint

alunos = []

for i in range(1,5):
    aluno = input('Digite o nome do aluno: ')
    alunos.append(aluno)

ordem = randint(0,3)
escolhido = choice(alunos) # feito no exercicio

print('O aluno sorteado foi o: {}'.format(alunos[ordem]))
print('O aluno sorteado foi o: {}'.format(escolhido))
