print("entre com os nomes e coloque em ordem alfabética crescente\n")
nomes = []
quantidade = int(input("Quantos nomes deseja inserir? "))
for i in range(quantidade):
    nome = input(f"{i+1}º Nome: ")
    nomes.append(nome)
nomes.sort() #sort serve para colocar em ordem alfabética
print(f"Nomes em ordem alfabética {nomes}")
nomes.sort(reverse=True) #reverse=True serve para colocar em ordem alfabética decrescente
print(f"Nomes em ordem alfabética descrescente {nomes}")

nome_remover = input("Escolha um nome para remover: ") #remove serve para remover um nome da lista
nomes.remove(nome_remover)
print(f"Nomes: {nomes}")