print('--DESAFIO 026--')
f = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparace {} vezes na frase. '.format(f.count('A')))
print('A primeira letra A apareceu na posição {}'.format(f.find('A')+1))
print('A últimna letra A apareceu na posição {}'.format(f.rfind('A')+1))