# Treinando funções

def pulaLinha():
    print("\n")


def lernotas():
    n = float(input("Digite uma Nota para o aluno(a): "))
    pulaLinha()
    return n


def resultado(n1, n2):
    media = (n1 + n2)/2
    print("Nota 1: ", n1)
    pulaLinha()
    print("Nota 2: ", n2)
    pulaLinha()
    print("Média: ", media, "Resultado: ", end="")
    if media >= 7:
        print("Aprovado, parabéns!")
    else:
        print("Reprovado.")
    pulaLinha()   

 
a = lernotas()
b = lernotas()
resultado(a, b)
