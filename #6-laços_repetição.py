# Treinando sistemas de repetição (for e while)

# FOR
for n in range(45, 42, -1):
    print(n)

# while

x = 1
while x <= 15:
    print(x)
    x = x+2

name = input("Digite seu nome por gentileza: ")
while(name ==int or name== float):
    name = input("Digite apenas nomes por gentileza: ")


qtd = 0
soma = 0
media = 0
valor = float(input("\nDigite um valor:"))

while(valor > 0.0):
    soma = soma+valor
    qtd = qtd+1
    # entrada de valores no loop
    valor = float(input("\nDigite um valor:"))

# digitando algum valor negativo o laço encerra
media = soma/qtd
print("\nTotal da soma: ", soma)
print("\n quantidade de numeros digitados: ", qtd)
print("\n Média dos valores: ", media)