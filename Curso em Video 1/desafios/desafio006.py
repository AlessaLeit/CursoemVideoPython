print('--DESAFIO 006--')
n = int(input('Digite um número:'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro do número inserido é {}, o triplo {} e a raiz quadrada {:.2f}'.format(d, t, r))
# Pra raiz da pra usar com a função de power dentro do format -> pow(n, 1/2))