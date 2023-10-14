print('='*8, 'MEDIDOR DE IMC - ÍNDICE DE MASSA CORPORAL' ,'='*8)

peso = float(input('Informe o Peso(Kg): '))
altura = float(input('Informe a altura(m): '))
imc = peso / (altura ** 2)
print('Seu IMC é de: {:.2f}  '.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif imc >= 18.5 and imc <= 25:
    print('Você está no seu PESO ÍDEAL!')
elif imc >= 25 and imc <= 30:
    print('Você está com SOBREPESO!')
elif imc >= 30 and imc <= 40:
    print('Você está com OBESIDADE, cuidado!')
else:
    print('Você está com OBESIDADE MÓRBIDA, cuidado!')

print('='*46)
