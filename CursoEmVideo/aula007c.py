n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
su = n1 - n2
p = n1**n2
r = n1%n2
i = n1//n2

print('Soma {} \nMultiplicacao {} \nDivisao {:.4f} \nSubtração {} \nPotencia {}'.format(s, m, d, su, p), end=' ')
print('Resto Divisao {} Divisao Inteira {}'.format(i,i))
print('Raiz quadrada {}'.format(81**(1/2)))
print('Raiz cubica {}'.format(81**(1/3)))

# pow(n1, (1/2)) outra forma de raiz quadrada