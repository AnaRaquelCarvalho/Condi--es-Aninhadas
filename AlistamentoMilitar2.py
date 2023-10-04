print('='*8 ,' Alistamento Militar ' ,'='*8)
nasc = int(input('Ano de Nascimento: '))
idade = 2023 - nasc
tempo = 18 - idade
temp = idade - 18
ano = nasc + 18
print('Quem nasceu em {} tem {} anos em 2023.'.format(nasc, idade))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    print('Ainda falta {} anos para o alistamento.'.format(tempo))
    print('Seu alistamento será em {}'.format(ano))
else:
    print('Você já deveria ter se alistado há {} anos'.format(temp))
    print('Seu alistamento foi em {}'.format(ano))

print('='*44)