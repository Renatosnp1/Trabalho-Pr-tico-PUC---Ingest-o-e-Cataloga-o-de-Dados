

class Atividade:

# f.	Dados de atividades realizadas pelo aluno:
        # i.	Matrícula do aluno
        # ii.	Código do curso
        # iii.	Código da disciplina
        # iv.	Período
        # v.	Código da atividade (número sequencial de acordo com a atividade)
        # vi.	Nome da atividade (Exercício | Trabalho | Avaliação)
        # vii.	Valor da atividade
        # viii.	Nota obtida pelo aluno


    def __init__(self,  id_aluno: int,
                        id_curso:int,
                        id_disciplina: int,
                        periodo: int,
                        id_atividade: int,
                        nome_atividade: str,
                        valor_atividade: float,
                        nota_atividade: float) -> None:


        self.id_aluno = id_aluno

        self.id_curso = id_curso

        self.id_disciplina = id_disciplina

        self.periodo = periodo

        self.id_atividade = id_atividade

        self.nome_atividade = nome_atividade

        self.valor_atividade = valor_atividade

        self.nota_atividade = nota_atividade