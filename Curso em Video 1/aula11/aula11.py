print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[0;34;47mOlá, Mundo!\033[m')
print('\033[7;34;47mOlá, Mundo!\033[m')
a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
cores = {'roxo':'\033[35m',
         'azul':'\033[34m',
         'limpa':'\033[m'}
print('Os valores são \033[0;35;40m{}\033[m e \033[7;35;40m{}\033[m'.format(a, b))
print('Os valores são {}{}{} e {}{}{}'.format('\033[7;35;40m', a, '\033[m', '\033[;35;40m', b,'\033[m)'))
print('Os valores são {}{}{} e {}{}{}'.format(cores['roxo'], a, cores['limpa'], cores['azul'], b, cores['limpa']))
