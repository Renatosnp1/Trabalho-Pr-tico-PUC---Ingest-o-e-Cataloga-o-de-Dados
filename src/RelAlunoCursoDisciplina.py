from typing import Literal


class RelacionamentoAlunoCursoDisciplina:

# e.	Dados de relacionamento entre alunos, cursos e disciplinas:
        # i.	Código do curso
        # ii.	Código da disciplina
        # iii.	Período (mm/aaaa)
        # iv.	Matrícula do aluno
        # v.	Nota do aluno
        # vi.	Frequência do aluno
        # vii.	Status (aprovado | reprovado | exame especial)
        # viii.	Motivo reprovação (nota | frequência)


    def __init__(self,  id_curso: str, 
                        id_disciplina: str, 
                        periodo: int, 
                        id_aluno:int, 
                        nota_aluno: float,
                        frequencia_aluno: int,
                        status: str,
                        motivo_reprovacao: Literal['Nota', 
                                                   'Frequencia'
                                                   ]) -> None:

        self.id_curso = id_curso

        self.id_disciplina = id_disciplina

        self.periodo = periodo

        self.id_aluno = id_aluno

        self.nota_aluno = nota_aluno

        self.frequencia_aluno = frequencia_aluno

        self.status = status

        self.motivo_reprovacao = motivo_reprovacao