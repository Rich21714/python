'''Na Escola de Magia de Python, os necromantes estão praticando a arte 
da necromancia e também precisam organizar sua vasta coleção de livros de necromancia. 
Eles devem criar um programa Python que lhes permita reviver e controlar esqueletos mágicos, 
ao mesmo tempo em que gerenciam sua biblioteca de livros.

Os necromantes devem criar variáveis individuais para representar os nomes 
dos esqueletos e seus estados (vivo ou morto). Cada esqueleto deve ser representado 
por uma variável de nome e uma variável de estado.

Os necromantes devem escrever uma função Python que permita a eles
 reviver um esqueleto morto. A função deve receber como entrada o nome 
 do esqueleto a ser revivido e alterar seu estado de "morto" para "vivo".

Os necromantes devem criar um loop while que permita que eles controlem 
seus esqueletos. Eles devem ser capazes de escolher entre as seguintes opções:
Reviver um esqueleto morto (escolhendo pelo nome).
Fazer com que um esqueleto ataque (escolhendo pelo nome).
Listar todos os esqueletos e seu estado atual.
Organizar sua coleção de livros de necromancia.
Sair do programa.
Os necromantes devem criar uma lista de livros de necromancia que eles possuem. 
Cada livro deve ser representado como uma string com o título do livro. 
Eles devem ser capazes de escolher a opção de organização e exibir todos os livros que possuem.
Utilização de variáveis para representar esqueletos e estados.
Implementação de funções para realizar a necromancia.
Utilização de loops while para criar um menu interativo de controle necromântico e organização de livros.
Aplicação de operadores lógicos e estruturas condicionais para tomar decisões mágicas.
Os necromantes devem demonstrar suas habilidades em Python enquanto 
revivem e controlam seus esqueletos mágicos e organizam sua coleção de livros de necromancia,
 dominando a arte da necromancia com código e mantendo seus conhecimentos bem organizados.'''

from random import randint
print("💥"*70)
print('Bem vindo ao mundo Magico')
print('Voce encontra esqueleto no caminho, gostaria de revive-lo?')
reviverEsqueleto = int(input('''
Digite [1]  - Vivo
Digite [2]  - Morto
Faça a escolha'''))
print(f'Digite sua opção')

if (reviverEsqueleto == 1):
    print(f'Obrigado, agora podemos trilhar em busca de novos membro para agregar nossa equeipe e desvendar novos caminhos')
    print(f' Ate chegarmos ao poço de magica aonde podemos distribuir a magia em nosso mundo e todos poderão festejar alegremente')
elif(reviverEsqueleto == 2):
    print(f'VOCÊ CAVOU MINHA COVA, agora nosso mundo esta perdido') 

if (reviverEsqueleto == 1):
    print(f'Ao caminhar encontramos um vale da morte aonde muitos antepassados vieram e não sobreviveram')
    print(f'seria uma tremenda fatalidade, ao passar chegará ao poço magico')

elif(reviverEsqueleto == 2):
    print(f'Atragetoria nunca foi facil, voce caiu no vale da morte e assim foi seu fim')    


 