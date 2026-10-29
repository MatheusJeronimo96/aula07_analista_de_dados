'''
Construa um algoritmo que tenha a entrada de números inteiros escolhidos pelo usuário. A quantide será escolhida, pelo usuário e o algoritmo mostrará
1 - uma lista com todos os números
2 - uma lista com números impares
3 - uma lista com números em ordem crescente
4 - uma lista com números em ordem decrescente
5 - uma lista com um número removido pelo usuário
'''

numeros = []
quantidade = int(input("quantos números deseja inserir? "))
for i in range(quantidade):
    numero = int(input(f"Digite o {i+1}º numero: "))
    numeros.append(numero)
numeros.sort()
print(f"numeros digitados: {numeros}")
numeros.sort(reverse=True)
print(f"numeros em ordem decrescente: {numeros}")

for i in numeros:
    if i %2 !=0:
        print(i)

numero_remover = int(input("escolha um numero para remover: "))
numeros.remove(numero_remover)
numeros.sort(reverse=False)
print(f"numeros: {numeros}")

