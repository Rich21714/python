''' CALCULO DE MEDIA  ANO / MES / DIA AVERAGE VERSION 1.0'''
print("💥"*75)
print(''' Calculo de media''')
soma = 0
i =1
while True:
    soma += float(input(f'''Digite a nota {i}:''').replace(',','.'))
    sair = ""
    while sair != 'S' or sair != 'N':
        sair = str(input('Quer sair do programa [S] iy [N]:').upper().strip()[0])
        if sair == 'S':
            break
        elif sair == 'N':
            break
        if sair == 'S':
            break
        elif sair == 'N':
            print()
        i += 1

    print(f'Valor de i é {i}')
    media = soma/i
    print(f'''A media é {media:.2f}''')
    print('FIM')
    print("💥"*75)
    


    