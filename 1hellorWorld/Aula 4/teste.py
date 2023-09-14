from datetime import date

nome = str(input("Olá qual é seu nome?\nDigite aqui: "))

dia = date.today().day
mes = date.today().month
anoAtual = date.today().year
diaNascimento = int(input('Dia de Nascimento:'))
mesNascimento = int(input('Mês de Nascimento:'))
anoNascimento = int(input('Ano de Nascimento:'))
print(f'{dia}/{mes}/{anoAtual}')
if(mesNascimento <= mes):
    print('O mes de nascimento é menor que o mes atual')
    
else:
    print('O mes de nascimento é maior que mes atual')
    print('NAO FIZ ANIVERSARIO')













