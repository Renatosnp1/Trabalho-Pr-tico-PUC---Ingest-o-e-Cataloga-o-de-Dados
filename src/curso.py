from typing import Literal
import random


class Curso:

    # b.	Dados dos cursos ofertados:
    # i.	ENGENHARIA DE COMPUTAÇÃO
    # 1.	Código do curso: 1
    # 2.	Períodos: 10
    # 3.	Carga horária prevista por disciplina: até 92 horas
    # 4.	Disciplinas por período: 8
    # 5.	Média de alunos por turma: 50

    def __init__(self,  id_curso: str,
                 nome_curso: str,
                 periodo: int,
                 alunos_por_turma: int,
                 disciplica_por_periodo: int,
                 nota_corte: int,
                 carga_horaria_prevista: int) -> None:

        self.alunos = []

        self.id_curso = id_curso

        self.nome_curso = nome_curso

        self.periodo = periodo

        self.carga_horaria_prevista = random.randint(
            16, carga_horaria_prevista)

        self.tipo = random.choice(['Teorica', 'pratica'])

        self.frequencia_minima = self.carga_horaria_prevista * 0.75

        self.alunos_por_turma = alunos_por_turma

        self.disciplica_por_periodo = disciplica_por_periodo

        self.nota_corte = nota_corte

    def __str__(self) -> str:
        return f"""=====================================================
ID_CURSO: {self.id_curso}
NOME_CURSO: {self.nome_curso}
CARGA_HORARIA: {self.carga_horaria_prevista}
TIPO: {self.tipo}
FREQ_MINIMA: {self.frequencia_minima}
ALUNOS_POR_TURMA: {self.alunos_por_turma}
DISCIPLINA_POR_PERIODO: {self.disciplica_por_periodo}
NOTA_CORTE: {self.nota_corte}
====================================================="""
