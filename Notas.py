print('='*16,'Média Final ','='*16)
n1 = float(input('Informe a 1ªnota: '))
n2 = float(input('Informe a 2ªnota: '))
n3 = float(input('Informe a 3ªnota: '))
n4 = float(input('Informe a 4ªnota: '))
media = (n1 + n2 + n3 + n4)/4
print('Tirando {:.1f} , {:.1f}, {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1,n2,n3,n4,media))
if media > 7.0:
    print('Aluno APROVADO!')
elif media >= 5.0 and media <= 6.9:
    print('O Aluno pegou RECUPERAÇÃO')
elif media < 5.0:
    print('Aluno REPROVADO!')

print('='*46)