# import math
from math import sqrt,floor

num = int(input('Digite um numero: '))

# raiz = math.sqrt(num)
raiz = sqrt(num)

print('A raiz de {} é igual a {:.2f}'.format(num,floor(raiz)))
