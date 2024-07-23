n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
print('PARÁBENS!!' if media > 6 else 'ESTUDE MAIS!')
if media <= 6:
    print('Você pegou recuperação, com {} de média!'.format(media))
else:
    print('Você passou com {} de média!'.format(media))
