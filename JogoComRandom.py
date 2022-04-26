from random import randint
from time import sleep
computador = randint(0, 5) #Comando que faz o computador pensar
print('-=-' *20)
print('Pensei em um número entre 0 e 5, tente adivinhar...')
print('-=-' *20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar"
print('PROCESSANDO...')
sleep (2)
if jogador == computador:
    print('Acertô, miserávi!')
else:
    print('Eu pensei no nº {}, não no nº {}! Tente outra vez xD'.format(computador,jogador))
