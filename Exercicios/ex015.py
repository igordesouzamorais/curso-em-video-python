km_percorrido = float(input('Quantos KMs foram percorridos ? '))
dias_alugados = int(input('Quantos dias de aluguel ? '))

pagar = (km_percorrido * 0.15) + (dias_alugados * 60)

print('O valor a ser pago é R${}'.format(pagar))
