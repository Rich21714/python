
from time import sleep

print('#'*50)
print('Você é um homem e seu objetivo é voltar para a sua vila, sua habilidade é a necromancia.')
print('Voltando para sua vila você encontra um esqueleto, gostaria de revive-lo?')
escolhaPlayer = int(input('''
Digite [1] -  SIM
Digite [2] -  NÃO
Faça a escolha: '''))
if (escolhaPlayer == 1):
    print('Você tira os esqueletos dentre os mortos, fazendo ele lutar uma ultima vez.')
    sleep(2)
    print('Você caminha por aquele por aquele bosque escuro mas tudo ficara bem enquanto o seu servo estiver ao seu lado')
    sleep(3)
    print('Seguindo o seu caminho você encontra uma cabana, a luz dentro dela')
    cabanaIluminada = int(input('''
    Digite [1] - SIM
    Digite [2] - NÃO
    Entrar na cabana? '''))
    if(cabanaIluminada == 1):
        print('Você decide entrar na cabana')
        esqueleto = int(input('''
        Digite [1] - SIM
        Digite [2] - NÃO
        Pode ser que alguma pessoa se assuste com o seu servo, entra com ele mesmo assim? '''))
        if(esqueleto == 1):
            print('Você entra com o seu esqueleto e uma criatura salta da escudidão com medo do esqueleto, é um goblin')
            sleep(2)
            print('Sem saber oque fazer o goblin te ataca com uma faca, por sorte o seu esqueleto te proteje do ataque dele e o ataca logo em seguida')
            sleep(2)
            print('Você decide correr pela janela quando ouve vozes vindo de fora da cabana')
            sleep(2)
            print('Quando você e seu esqueleto se afastam o suficiente você da uma pausa para respirar ')
            print('Depois de um tempo de caminhada você chega na vila e é recebido pela sua mulher e sua filha')
            sleep(2)
            print(f'\033[31mVOCÊ VENCEU\033[m')
        elif(esqueleto == 2):
            print('Enquanto você entra na cabana o seu esqueleto o espera do lado de fora')
            print('Entrando lá você ve uma sombra de algo parecido com um humano')
            print('Está sombra te chama e fala para você se sentar perto do fogo')
            sombraMisteriosa = int(input('''
            Digite [1] - SIM
            Digite [2] - NÃO
            Se sentar? '''))
            if(sombraMisteriosa == 1):
                print(' Um goblin salta das sombras e te apunhala, você empurra a criatura para longe porem acaba desmaiando por conta da perca de sangue')
                print('... Você morreu')
                print('Não se deve confiar em estranhos, tente novamente.')
            elif(sombraMisteriosa == 2):
                print('Você decide não ficar e a sombra se meche para mais perto')
                sleep(2)
                print('Com medo de ser atacado você ordena que o seu servo entre na cabana, porem antes de seu esqueleto entrar salta da sombra uma criatura e te acerta com uma lamina')
                sleep(2)
                print('A criatura ignora o esqueleto e avança mais uma vez em você, porem é impedido pelo esqueleto, que acaba matando o goblin ali mesmo')
                sleep(2)
                print('Você decide correr pela janela quando ouve vozes vindo de fora da cabana')
                sleep(2)
                print('Quando você e seu esqueleto se afastam o suficiente você da uma pausa para respirar')
                print('Depois de um tempo de caminhada você chega na vila e é recebido pela sua mulher e sua filha')
                sleep(2)
                print(f'\033[31mVOCÊ VENCEU\033[m')
    elif(cabanaIluminada == 2):
        print('Você apenas passa reto pela cabana')
        sleep(2)
        print('porem não muitos passos depois vocês acaba caindo em uma armailha e ficam suspensos em uma arvore')
        sleep(3)
        print('Quando você percebe foi rodeado por goblins')
        sleep(2)
        print('Você está correndo perigo mas percebe que o antebraço do seu servo é pontudo')
        antebraçoEsqueleto = int(input( '''
        Digite [1] - SIM
        Digite [2] - NÃO
         Sacrificar o braço do seu esqueleto? Isto fará ele cair para os goblins '''))
        if(antebraçoEsqueleto == 1):
            print('Com um leve aperto em seu coração você sacrifica o seu esqueleto pegando o seu braço e usando para cortar as cordas')
            sleep(3)
            print('O esqueleto cai para os goblins para a sobrevivencia de seu mestre...')
            sleep(2)
            print('Usando o osso você consegue se soltar e fugir, porem é imobilizado por uma armadilha de urso')
            sleep(2)
            print('... Você morreu')
            print('Talvez tenha sido o preço a ser pago pela vida de seu servo')
        elif(antebraçoEsqueleto == 2):
            print('Se recusando a sacrificar um aliado você começa a roer as cordas que o prendia a arvore')
            sleep(3)
            print('De repente você houve um barulho vindo da floresta')
            sleep(2)
            print('São caçadores da sua vila!')
            sleep(2)
            print('Os goblins ao ver aquilo fogem e você e seu esqueleto são resgatados')
            sleep(2)
            print(f'\033[31mVOCÊ VENCEU\033[m')
elif(escolhaPlayer == 2):
    print('Você apenas passa pelo esqueleto, seguindo a sua jornada')
    sleep(2)
    print('a solidão te confronta')
    sleep(2)
    print('Andando naquela solidão você encontra uma cabana iluminada, será que é seguro entrar nela?')
    cabanaIluminada = int(input('''
    Digite [1] - SIM
    Digite [2] - NÃO
    Entra na cabana? '''))
    if(cabanaIluminada == 1):
        print('Com relutancia você decide entrar na cabana')
        sleep(2)
        print('Entrando lá você ve uma sombra de algo parecido com um humano')
        sleep(2)
        print('Está sombra te chama e fala para você se sentar perto do fogo')
        sombraMisteriosa = int(input('''
        Digite [1] - SIM
        Digite [2] - NÃO
        Se sentar? '''))
        if(sombraMisteriosa == 1):
            print(' Um goblin salta das sombras e te apunhala, você empurra a criatura para longe porem acaba desmaiando por conta da perca de sangue... Você morreu')
            print('Não se deve confiar em estranhos, tente novamente.')
        elif(sombraMisteriosa == 2):
            print('Você recusa educadamente enquanto se afasta, quando você decide sair a porta da cabana bate com força e você ouve passos vindo por tras')
            sleep(2)
            print('Quando você se vira é tarde demais, um goblin aparece e te acerta com uma lamina')
            sleep(2)
            print('... Você morreu')
            print('Não entre em lugares desconhecidos sem poder se defender.')
    elif(cabanaIluminada == 2):
        print('Você apenas passa pela cabana, seguindo o seu caminho')
        sleep(2)
        print('Não muitos passos depois de passar pela cabana você acaba caindo em um buraco fundo')
        sleep(2)
        print('Oque é isso? uma armadilha?')
        sleep(2)
        print('Você ouve passos e risadas cercando o buraco')
        sleep(2)
        print('Você foi pego por goblins que ficam bravos pois pensaram que tinham pego algum animal')
        sleep(2)
        print('Como vingança os goblins começam a tapar o buraco com você ainda nele')
        sleep(2)
        print('... Você morreu')
        print('Será que a cabana era a escolha certa? Tente Novamente')