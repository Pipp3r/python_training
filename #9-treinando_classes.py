

class Carro:
#classe que simula o funcionamento de um carro
    def __init__(self):

        self.velocidadeAtual = 0
        self.cor = "vermelho"

#testando a classe carro
    def acelera(self):
        self.velocidadeAtual = self.velocidadeAtual + 1

    def freia (self):
        self.velocidadeAtual = self.velocidadeAtual - 1

    def mudaCor(self, nomeCor):
        self.cor = nomeCor

    def retornaVelocidadeAtual(self):
        return self.velocidadeAtual

    def retornaCor(self):
        return self.cor

#acelerando e mudando de cor
meuCarro = Carro()
meuCarro.mudaCor("verde")
meuCarro.acelera()
meuCarro.acelera()
meuCarro.acelera()
meuCarro.acelera()
meuCarro.acelera()
meuCarro.acelera()
meuCarro.acelera()
meuCarro.acelera()
meuCarro.acelera()
meuCarro.acelera()
print("\nvelocidade acelerando: ", meuCarro.retornaVelocidadeAtual())
print("\n")
meuCarro.freia()
print("\nFreiou: ", meuCarro.retornaVelocidadeAtual())
print("\n")
print("Cor inicial: ", meuCarro.retornaCor())
meuCarro.mudaCor("azul")
print("\nmudança de cor: ", meuCarro.retornaCor())
print("\n")