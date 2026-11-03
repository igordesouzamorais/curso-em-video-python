frase = 'Curso em Vídeo Python'
print(frase)
print(frase[9])
print(frase[9:13]) # o 13 nao entra na busca, vai ate o 12 apenas
print(frase[9:21:2]) # vai ate o 20 e pula de 2 em 2
print(frase[:5]) # sem informar comeca do 0
print(frase[15:]) # vai ate o final da string
print(frase[9::3]) # vai do 9 ate o final pulando de 3 em 3
print(len(frase))
print(frase.count('o')) # conta os caracteres
print(frase.count('o', 0, 13)) # conta apenas do zero ao 12
print(frase.find('deo')) # retorna posicao inicial da busca
print(frase.find('Android'))
print('Curso' in frase)
