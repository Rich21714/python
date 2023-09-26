print("❓"*75)
print('Numero primo')
numero = int(input(f'Digite um '))
if numero == 1:
    print(f'Numero: {numero} é primo')
elif numero == 2:
    print(f'Numero: {numero} é o unico primo par')
for i in range(1, numero+1):
    print(f'{numero}/{i}={numero%i}')
    
    
