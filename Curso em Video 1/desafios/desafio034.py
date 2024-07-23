print('--DESAFIO 034--')
sal = float(input('Digite seu salário: '))
if sal > 1250.00:
    au = sal + (sal * 0.1)
    print('Você recebeu 10% de aumento, agora você recebe {:.2f}'.format(au))
else:
    au = sal + (sal * 0.15)
    print('Você recebeu 15% de aumento, agora você recebe {:.2f}'.format(au))