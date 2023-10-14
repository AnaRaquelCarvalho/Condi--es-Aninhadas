print('='*8, 'Lojas Carvalho - Formas de Pagamentos' ,'='*8,)

preco = float(input('Preço das Compras(R$) '))
print('='*16, 'FORMAS DE PAGAMENTOS' ,'='*16)
print('[1] À vista Dinheiro/Cheque.')
print('[2] À vista no Cartão.')
print('[3] 2X no Cartão.')
print('[4] 3x ou mais vezes no Cartão.')

opcao = int(input('Opção: '))
if opcao == 1:
    vista = preco - (preco * 10 / 100)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, vista))
elif opcao == 2:
    cartao = preco - (preco * 5 / 100)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(preco, cartao))
elif opcao == 3:
    nominal = preco
    parcela = nominal / 2
    print('Compra parcelada em 2 vezes de R$ {:.2f} Sem Juros.'.format(parcela))
elif opcao == 4:
    parcelas = preco + (preco * 20 / 100)
    n1 = int(input('Número de Parcelas: '))
    ValorParc = parcelas / n1
    print('Sua compra parcelada em {} de R$ {:.2f}.'.format(n1,ValorParc))
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} com juros no cartão'.format(preco, parcelas))
else:
    opcao = 0
    print('\033[1:31m[{}]'.format(opcao),'>>> OPÇÃO INVÁLIDA de Pagamento, TENTE NOVAMENTE!')

print('='*76)




