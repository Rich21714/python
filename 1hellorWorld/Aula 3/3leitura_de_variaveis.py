'''
LEITURA DE VARIAVEIS O USUARIO PODERÁ DIGITAR VALORES VIA TECLADO
. OBS OS VALORES SEMPRE SERÃO TIPO STRING, É IMPORTANTE SEMPRE
CONVERTER PARA UMA VARIAVEL NUMERICA CASO
SEJA NECESSARIO FAZER ALGUM TIPO DE OPREÇÃO MATEMAICA

'''

pensamento = input("Meu pensamento:")
print(pensamento, type (pensamento))


x = int(input("digite o numero 1: "))
y = int(input("digite o numero 2: "))
r = x + y 
print(f"O resultado é {r}")