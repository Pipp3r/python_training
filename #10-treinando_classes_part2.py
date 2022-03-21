# Criando a classe alunos para parametrizar dados

class Alunos:

    def __init__(self, matricula=200850, nome="Fernando Pipper de Almeida", nota1=float(10), nota2=float(0), notatrabalho=float(10)):
        self.nota_1 = nota1
        self.nota_2 = nota2
        self.nota_trabalho = notatrabalho
        self.ra = matricula
        self.nome_aluno = nome
        self.media = 0

    def pula_linha(self):
        print("\n")

    def media_alunos(self):
        self.media = (self.nota_1 * 0.25) + \
            (self.nota_2 * 0.25)+(self.nota_trabalho*0.2)
        return self.media

    def nota_final(self, final):
        nota_af = 0
        if final >= 5:
            print("Situação: Aprovado.")
            print("Parabéns, você foi aprovado! Sua média foi: %.2f" % final,)
            print("Não precisa fazer A.F\n")
        else:
            print("Situação: Reprovado.\nSua nota atual é: %.2f" % final)
            final = float((5 - final)/0.3)
            print("você precisa de: %.2f na avaliação final.\n" % final)

    def exibicao(self):
        print("\nNome do aluno: ", self.nome_aluno, "\n")
        print("R.A do aluno: ", self.ra)


Aluno1 = Alunos()
Aluno1.exibicao()
Aluno1.pula_linha()
media_geral = Aluno1.media_alunos()
Aluno1.nota_final(media_geral)
