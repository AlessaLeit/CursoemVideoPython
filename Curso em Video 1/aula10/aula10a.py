nome = str(input('Qual é seu nome? '))
if nome == 'Alessandra':
    print('Que nome bonito!')
else:
    print('Que nome normal!')
# print('Que nome bonito!' if nome == 'Alessandra' else 'Que nome normal!')
print('Bom dia {}'.format(nome))
