altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))

area = altura * largura
tinta = area / 2

print('Para pintar uma parede de {}M2 é necessário de {}LT de tinta'.format(area, tinta))
