print('--DESAFIO 033--')
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))
num = [n1, n2, n3]
num.sort()
print('O maior número é {} e o menor é {}'.format(num[2], num[0]))
