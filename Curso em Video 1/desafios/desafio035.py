print('--DESAFIO 035--')
r1 = float(input('Digite o valor da 1ª reta: '))
r2 = float(input('Digite o valor da 2ª reta: '))
r3 = float(input('Digite o valor da 3ª reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')

'''Como eu tinha feito
retas = [r1, r2, r3]
retas.sort()
doislado = retas[0] + retas[1]
if doislado >= retas[2]:
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')'''
