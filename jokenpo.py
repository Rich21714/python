''' EXERCICIO JO-KEN-PO , O JOGADOR ESCOLHERA 
PEDRA PAPEL E TESOURA E O COMPUTADOR TAMBEM 
ATRAVES DE UM NUMERO ALEATORIO DE 1 A 3 ALUNOS DE PYTHON 18/09/23 VERSION 1.0'''

from random import randint
from time import sleep
print('#'*50)
print(''' BEM VINDO AO JOGO DO JO-KEN-PO  ✊✋✌️ 😎💨 ''')
sleep(1)
print("JO-✊")
sleep(1)
print("ken-✋")
sleep(2)
print("Po-✌")
sleep(3)




escolhaPlayer = int(input('''
Digite [1] - ✊ - PEDRA
Digite [2] - ✋ - PAPEL
Digite [3] - ✌️ - TESOURA
Faça a escolha'''))
print(f'Sua escolha foi: {escolhaPlayer} ')
acumularPonto = 0 

if (escolhaPlayer == 1):
    print(f'Asua escolha foi ✊')
elif(escolhaPlayer == 2):
    print(f'A sua escolha foi ✋')
elif(escolhaPlayer == 3):
    print(f'A sua escolha foi ✌ ')
else:
    print('Digite uma opcao de 1 a 3 e reinicie novamente')
#escolha do computador
escolhadoPC = randint(1,3)
if (escolhaPlayer == 1):
    print(f'O Computador escolheu  ✊')
elif(escolhaPlayer == 2):
    print(f'O Computador escolheu  ✋')
else:

    print(f'O Computador escolheu  ✌ ')
if(escolhaPlayer == escolhadoPC):
    print(f'''EMPATE''')

#PEDRA GANHA DE TESOURA = 1 GANHA DE 3
#PAPEL GANHA DE PEDRA = 2 GANHA DE 1
#TESOURA GANHA DE PAPEL = 3 GANHA DE 2 

elif((escolhaPlayer  == 1 and escolhadoPC  == 3) or 
     (escolhaPlayer  == 2 and escolhadoPC == 1) or
     (escolhaPlayer  == 3 and escolhadoPC == 2)):
    print( ''' PARABENS VOCE GANHOU ''')
    acumularPonto += 1
    print(f''' Sua pontuacao é {acumularPonto}''')

else: 
    print(''' GAME OVER ''')