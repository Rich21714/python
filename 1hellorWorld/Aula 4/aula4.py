nome = str(input("digite seu nome: "))
ano_nasci = int(input("Digite ano de Nascimento: "))
ano_atual = int(input("Digite o ano atual: " ))
r = ano_atual - ano_nasci
print(f" Sua idade é {r}")

ano_nasci = True
ano_atual = 0
nome = str(input('Nome do Personagem:\n'))
if((nome == nome and ano_nasci == True)or(nome == ano_atual and ano_nasci== True)):
    ano_atual = ano_atual + 1
    print(f'{nome} pegou a moeda e teve {ano_atual}')
    moeda = str(input("Deseja prgar mais moeda?\n"))
else:
    print(f'Não pegou a moeda')
