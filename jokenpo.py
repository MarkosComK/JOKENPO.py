import sys
from random import randint
from time import sleep
print('===========JOKENPO===========')
print('''Suas opções:
[ 0 ]PEDRA
[ 1 ]PAPEL
[ 2 ]TESOURA''')
jogador = int(input('Qual é sua jogada: '))
if jogador != 0 or 1 or 2:
    print('OPÇÃO INVÁLIDA')
    sys.exit()
pc = randint(0, 2)
sleep(1)
print('       JO')
sleep(1)
print('       KEN')
sleep(1)
print('       PO')
sleep(1)
print('-='*19)
if pc == 0:
    print('Computador jogou PEDRA')
if pc == 1:
    print('Computador jogou PAPEL')
if pc == 2:
    print('Computador jogou TESOURA')
if jogador == 0:
    print('Jogador jogou PEDRA')
if jogador == 1:
    print('Jogador jogou PAPEL')
if jogador == 2:
    print('Jogador jogou TESOURA')
print('-='*19)
if jogador - pc == 1:
    print('O jogador venceu a máquina!')
elif jogador - pc == 0:
    print('EMPATE!')
else:
    print('A máquina venceu!')