print('--DESAFIO 031--')
km = float(input('Qual a distância da sua viagem? '))
# p = km * 0.5 if km <= 200 else km * 0.45
if km <= 200:
    p = km * 0.5
else:
    p = km * 0.45
print('O preço da passagem por km é R$0.45')
print('No total sua viagem custará R${:.2f}'.format(p))