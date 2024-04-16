print('='*8,' Game Jokenpô - Pedra, Papel e Tesoura ','='*8)

import random
from random import randint
from time import sleep
itens = ('PEDRA','PAPEL','TESOURA')
computador = randint(0,2)

print('>>> OPÇÕES: <<<')
print('[0] PEDRA.')
print('[1] PAPEL.')
print('[2] TESOURA. ')
jogador = int(input('>>> Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÕ')
sleep(1)
print('-='*11)
print('Computador Jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))

print('-='*11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
print('-='*11)