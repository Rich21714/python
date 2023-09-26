import random

# Função para adicionar um item à mochila
def adicionar_item(mochila):
    nome_item = input("Digite o nome do item: ")
    poder_magico = random.randint(1, 100)  # Gerar poder mágico aleatório
    item = (nome_item, poder_magico)
    if poder_magico >= 0:
        mochila.append(item)
        print(f"{nome_item} foi adicionado à mochila.")
    else:
        print("Não é possível adicionar um item com poder mágico negativo.")

# Função para remover um item da mochila
def remover_item(mochila):
    if not mochila:
        print("A mochila está vazia.")
        return
    
    print("Itens na mochila:")
    for i, item in enumerate(mochila):
        print(f"{i + 1}: {item[0]} (Poder Mágico: {item[1]})")
    
    indice = int(input("Digite o número do item que deseja remover: ")) - 1
    if 0 <= indice < len(mochila):
        item_removido = mochila.pop(indice)
        print(f"{item_removido[0]} foi removido da mochila.")
    else:
        print("Número de item inválido.")

# Função para listar todos os itens na mochila
def listar_itens(mochila):
    if not mochila:
        print("A mochila está vazia.")
        return
    
    print("Itens na mochila:")
    for i, item in enumerate(mochila):
        print(f"{i + 1}: {item[0]} (Poder Mágico: {item[1]})")

# Função para encontrar o item mais poderoso na mochila
def encontrar_item_mais_poderoso(mochila):
    if not mochila:
        print("A mochila está vazia.")
        return None
    
    item_mais_poderoso = max(mochila, key=lambda x: x[1])
    return item_mais_poderoso

# Mochila mágica inicial vazia
mochila_magica = []

while True:
    print("\nEscola de Magia de Python - Mochila Mágica")
    print("1. Adicionar um item à mochila")
    print("2. Remover um item da mochila")
    print("3. Listar todos os itens na mochila")
    print("4. Encontrar o item mais poderoso na mochila")
    print("5. Sair do programa")
    
    escolha = input("Digite o número da opção desejada: ")
    
    if escolha == "1":
        adicionar_item(mochila_magica)
    elif escolha == "2":
        remover_item(mochila_magica)
    elif escolha == "3":
        listar_itens(mochila_magica)
    elif escolha == "4":
        item_mais_poderoso = encontrar_item_mais_poderoso(mochila_magica)
        if item_mais_poderoso:
            print(f"Item mais poderoso na mochila: {item_mais_poderoso[0]} (Poder Mágico: {item_mais_poderoso[1]})")
    elif escolha == "5":
        print("Obrigado por usar a Mochila Mágica! Adeus!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

