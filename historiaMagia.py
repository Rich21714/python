print('#'*50)

print('Você encontra um esqueleto em seu caminho, gostaria de revive-lo?')
escolhaPlayer = int(input('''
Digite [1] -  SIM
Digite [2] -  NÃO
Faça a escolha: '''))

if (escolhaPlayer == 1):
    print('Você levanta o esqueleto e ele te jura lealdade')
    print('Você caminha  por aquele bosque escuro mas tudo ficara bem enquanto o seu servo estiver ao seu lado')
    print('Seguindo o seu caminho rumo a vila mais proxima você encontra uma cabana, há luz dentro dela')
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
            print('Sem saber oque fazer o goblin te ataca com uma faca, por sorte o seu esqueleto te proteje do ataque dele e o ataca logo em seguida')
            print('Você decide correr pela janela quando ouve vozes vindo de fora da cabana.')
            print('Quando você e seu esqueleto se afastam o suficiente você da uma pausa para respirar ')
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
                print('Você decide não ficar e a sombra se mexer para mais perto')
                print('Com medo de ser atacado você ordena que o seu servo entre na cabana, porem antes de seu esqueleto entrar salta da sombra, uma criatura e te acerta com uma lamina')
                print('O goblin ignora o esqueleto e avança mais uma vez em você, porem é impedido pelo esqueleto, que acaba matando o goblin ali mesmo.')
                print('Você decide correr pela janela quando ouve vozes vindo de fora da cabana')
                print('Você se esconde')
               
                
    print('Depois de um tempo de caminhada você chega na vila e é recebido pela sua mulher e sua filha')
    print(f'\033[31mVOCÊ VENCEU\033[m')
elif(escolhaPlayer == 2):
    print('Você apenas passa pelo esqueleto, seguindo a sua jornada')
    print('a solidão te confronta')
    print('Andando naquela solidão você encontra uma cabana iluminada, será que é seguro entrar nela?')
    cabanaIluminada = int(input('''
    Digite [1] - SIM
    Digite [2] - NÃO
    Entra na cabana? '''))
    if(cabanaIluminada == 1):
        print('Com relutancia você decide entrar na cabana')
        print('Entrando lá você ve uma sombra de algo parecido com um humano')
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
            print('Quando você se vira é tarde demais, um goblin aparece e te acerta com uma lamina')
            print('... Você morreu')
            print('Não entre em lugares desconhecidos sem poder se defender.')
    elif(cabanaIluminada == 2):
        print('Você apenas passa pela cabana, seguindo o seu caminho')
        print('Não muitos passos depois de passar pela cabana você acaba caindo em um buraco fundo')
        print('Oque é isso? uma armadilha?')
        print('Você ouve passos e risadas cercando o buraco')
        print('Você foi pego por goblins que ficam bravos pois pensaram que tinham pego algum animal')
        print('Como vingança os goblins começam a tapar o buraco com você ainda nele')
        print('... Você morreu')
        print('Será que a cabana era a escolha certa?')
    
