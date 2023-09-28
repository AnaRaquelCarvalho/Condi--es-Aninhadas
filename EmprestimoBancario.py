print('='*6,' Simulador de Financiamento de Imobiliário ','='*6)
casa = float(input('Valor do Imóvel: R$ '))
salario = float(input('Informe sua renda familiar mensal: R$ '))
anos = int(input('Tempo de Financiamento: '))

Prestação = casa/(anos * 12)
minimo = salario * 30 / 100

print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end = '')
print(' a prestação será de R$ {:.2f}'.format(Prestação))

if casa <= minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO!')

print('='*64)