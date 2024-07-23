print('--DESAFIO 011--')
l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
area = l * a
tinta = area / 2
print('Parede de dimensão {}mx{}m tem área de {}m'.format(l, a, area))
print('A quantidade de tinta em litros que vai ser preciso é de {}l'.format(tinta))