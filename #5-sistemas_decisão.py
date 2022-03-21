# Treinando sistemas de decisão simples (if e else)

idade = float(input("digite a idade da pessoa:"))

if idade > 18 and idade<=110:
    print("a pessoa é maior de idade")
elif idade > 110 or idade < 0:
    print("digite um valor valído")
else:
    print("a pessoa é menor de idade")