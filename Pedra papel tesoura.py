import random
from time import sleep
print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
player = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
sleep(1)

pc = random.randint(0, 2)

if pc == 0 and player == 0:
    print('-=-' * 10)
    print('Computadr jogou PEDRA')
    print('Jogador jogou PEDRA')
    print('-=-' * 10)
    print('EMPATE')

elif pc == 0 and player == 1:
    print('-=-'*10)
    print('Computadr jogou PEDRA')
    print('Jogador jogou PAPEL')
    print('-=-' * 10)
    print('JOGADOR VENCE')

elif pc == 0 and player == 2:
    print('-=-' * 10)
    print('Computadr jogou PEDRA')
    print('Jogador jogou TESOURA')
    print('-=-' * 10)
    print('COMPUTADOR VENCE')



elif pc == 1 and player == 0:
    print('-=-' * 10)
    print('Computadr jogou PAPEL')
    print('Jogador jogou PEDRA')
    print('-=-' * 10)
    print('COMPUTADOR VENCE')

elif pc == 1 and player == 1:
    print('-=-' * 10)
    print('Computadr jogou PAPEL')
    print('Jogador jogou PAPEL')
    print('-=-' * 10)
    print('EMPATE')

elif pc == 1 and player == 2:
    print('-=-' * 10)
    print('Computadr jogou PAPEL')
    print('Jogador jogou TESOURA')
    print('-=-' * 10)
    print('JOGADOR VENCE')

elif pc == 2 and player == 0:
    print('-=-' * 10)
    print('Computadr jogou TESOURA')
    print('Jogador jogou PEDRA')
    print('-=-' * 10)
    print('JOGADOR VENCE')

elif pc == 2 and player == 1:
    print('-=-' * 10)
    print('Computadr jogou TESOURA')
    print('Jogador jogou PAPEL')
    print('-=-' * 10)
    print('COMPUTADOR VENCE')

elif pc == 2 and player == 2:
    print('-=-' * 10)
    print('Computadr jogou TESOURA')
    print('Jogador jogou TESOURA')
    print('-=-' * 10)
    print('EMPATE')

