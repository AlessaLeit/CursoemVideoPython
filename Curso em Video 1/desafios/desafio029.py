print('--DESAFIO 029--')
v = float(input('Qual a velocidade do carro? '))
if v > 80:
    print('Você está acima do permitido, você foi multado!')
    m = (v - 80) * 7
    print('Você precisa pagar um total de R${:.2f} de multa'.format(m))
else:
    print('Boa viagem, siga com cuidado e seguindo as normas de trânsito!')