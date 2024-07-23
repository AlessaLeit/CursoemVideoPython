from math import sin, cos, tan, radians
print('--DESAFIO 018--')
ang = float(input('Digite o ângulo: '))
seno = sin(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, seno))
cos = cos(radians(ang))
print('O ângulo de {} tem o COS de {:.2f}'.format(ang, cos))
tag = tan(radians(ang))
print('O ângulo de {} tem TANGENTE de {:.2f}'.format(ang, tag))