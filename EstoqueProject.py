# Definição de entrada de itens

def add_itens():
    print("Bem-vindo ao Estoque de Equipamentos!")
    nome = input("Digite o nome do item: ")
    quantidade = int(input(f"Quantidade de {nome}: "))
    descricao = input("Descrição: ")


    #Adicionando ao dicionário a informação

    return {"Nome": nome, "QTD": quantidade, "Desc": descricao}


# Criação do dicionário vazio

lista_estoque = []


# Adicão de Itens ao dicionário

item1 = add_itens()
lista_estoque.append(item1)

item2 = add_itens()
lista_estoque.append(item2)

"""
Append was used to enter a item in the final list

"""


print("\n Estoque Atual")
for item in lista_estoque:
    print(f"Item: {item['Nome']} | QTD: {item['QTD']} | Desc: {item['Desc']}")


