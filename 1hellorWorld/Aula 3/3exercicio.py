'''
1) Data de nascimento criar  um programa que pergunte ao usuario 
seu nome a data de seu nascimento e calcule a idade com base no ano atual;

2) crie um programa em que o usuario digite os valores e o programa calcule a base de um triagulo retangulo.

3) Crie um programa  que o usuario digite o peso e a altura e o programa calcule o IMC indice de massa corporal 

4)Crie um programa que o ususario digite um numero em graus celsius e o programa coverta em farenheith 

5) Faça o mesmo para farenheit em celsius 

6) Crie um programa que calcule baskara dos valores digitados regras a tem que ser sempre
 elevado ao quadrado x² mas a pode ter qualquer valor ax² + ou -bx + ou - c = 0 


'''

print("_"*50)
print("EXERCÍCIO 1")
##

nome = (input("digite seu nome: "))
ano_nasci= int(input("Digite ano de Nascimento: "))
ano_atual = int(input("Digite o ano atual: " ))
r = ano_atual - ano_nasci
print(f" Sua idade é {r}")

print("_"*50)
print("EXERCÍCIO 2")


# Solicita que o usuário digite o valor do primeiro cateto
cateto1 = float(input("Digite o valor do primeiro cateto: "))

# Solicita que o usuário digite o valor do segundo cateto
cateto2 = float(input("Digite o valor do segundo cateto: "))

# Calcula a hipotenusa (base) usando o teorema de Pitágoras
base = (cateto1*cateto2)/2

# Exibe o valor da base
print(f"A base do triângulo retângulo é: {base}")

print("_"*50)
print("EXERCÍCIO 3")

# Solicita que o usuário digite seu peso
peso = float(input("Digite seu peso : "))

# Solicita que o usuário digite sua altura
altura = float(input("Digite sua altura : "))

# Calcula a hipotenusa (base) usando o teorema de Pitágoras
imc = peso / (altura ** 2)

# Exibe 
print(f"O seu índice de massa corporal (IMC) é: {imc: .2f}")

print("_"*50)
print("EXERCÍCIO 4")

# Solicita que o usuário digite a temperatura em graus Celsius
celsius = float(input("Digite a temperatura em graus Celsius: "))
# Converte a temperatura de Celsius para Fahrenheit usando a fórmula: F = (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32
# Exibe a temperatura em Fahrenheit
print(f"A temperatura em graus Fahrenheit é: {fahrenheit:.2f}°F")

print("_"*50)
print("EXERCÍCIO 5")

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"A temperatura em graus Celsius é: {celsius:.2f}°C")


print("_"*50)
print("EXERCÍCIO 6")

# x² + x - 8
# a + b - c
 
a = int(input("A:"))
b = int(input("B:"))
c = int(input("C"))
delta = float(pow(pow(b,2)-4*a*c,1/2))
print(delta)
x1 = (-b + delta)/2*a
x2 = (-b - delta)/2*a 
print(f"x1 = {x1:.2f} e x2 ={x2:.2f}")






