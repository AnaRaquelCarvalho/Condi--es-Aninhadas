print('='*8,'Desafio dos Triãngulos','='*8)

n1 = float(input('1º Segmento: '))
n2 = float(input('2º Segmento: '))
n3 = float(input('3º Segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os Segmentos acima PODEM FORMAR UM TRIÂNGULO: ',end='')
if n1 == n2 == n3:
    print('EQUILÁTERO')
elif n1 != n2 != n3 != n1:
    print('Escaleno')
else:
    print('ISÓSCELES: ')
