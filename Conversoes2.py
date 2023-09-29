print('='*16,' Base de Conversão ','='*16)

n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção = int(input('Sua Opção: '))

if opção == 1:
    print('{} convertido para Binário é igual a {}'.format(n, bin(n) [2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n,oct(n)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n,hex(n)[2:]))
else:
    print('>>> Opção Inválida. Tente novamente. <<<')