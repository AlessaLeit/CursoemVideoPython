print('--DESAFIO 03--')
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
s = n1 + n2
cores = {
    'azul':'\033[34m',
    'vermelho':'\033[31m',
    'ciano':'\033[36m',
    'limpo':'\033[m'}
print('A soma entre {}{}{} e {}{}{} é igual a {}{}{}!'.format(cores['azul'],n1, cores['limpo'], cores['vermelho'], n2, cores['limpo'], cores['ciano'], s, cores['limpo']))
