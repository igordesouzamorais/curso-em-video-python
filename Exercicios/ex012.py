preco = float(input('Digite o valor do produto: '))
desconto = float(input('QUal o perentual de desconto: '))

novoPreco = preco - ( preco * (desconto / 100) )

print('O preco com desconto de {}% é: {:.2f}'.format(desconto, novoPreco))
