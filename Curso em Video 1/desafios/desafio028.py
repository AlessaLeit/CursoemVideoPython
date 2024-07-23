print('--DESAFIO 028--')
import random
from time import sleep
n = random.randint(0, 5)
c = int(input('Tente advinhar o número selecionado pelo programa (0 a 5): '))
print('PROCESSANDO...')
sleep(3)
if c == n:
    print('PARÁBENS!\nVocê é muito bom nisso')
else:
    print('Opa, não foi dessa vez')
print('Número selecionado: {}'.format(n))
print('Sua tentativa: {}'.format(c))