print('--DESAFIO 017--')
import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
'''hip = (co ** 2) + (ca ** 2)
print('O comprimento da hipotenusa é {:.2f}'.format(sqrt(hip)))'''
h = math.hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}'.format(h))
