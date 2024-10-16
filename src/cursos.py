from typing import Literal
import random


class Curso:

    def __init__(self) -> None:

        self.ID_CURSO = None
        self.NOME_CURSO = None
        self.HORAS = None
        self.PERIODOS = None
        self.DISCIPLINA = None
        self.PERIODO = None
        self.QTD_ALUNOS = None

    def get_curso_1(self):
        self.ID_CURSO = 1
        self.NOME_CURSO = 'ENGENHARIA DE COMPUTAÇÃO'
        self.HORAS = 92
        self.PERIODOS = 10
        self.DISCIPLINA_POR_PERIODO = 8
        self.TOTAL_DISCIPLINA = self.PERIODOS * self.DISCIPLINA_POR_PERIODO
        self.QTD_ALUNOS = 50

        return {'ID_CURSO': self.ID_CURSO,
                'NOME_CURSO': self.NOME_CURSO,
                'HORAS': self.HORAS,
                'PERIODOS': self.PERIODOS,
                'DISCIPLINA_POR_PERIODO': self.DISCIPLINA_POR_PERIODO,
                'TOTAL_DISCIPLINA': self.TOTAL_DISCIPLINA,
                'QTD_ALUNOS': self.QTD_ALUNOS}

    def get_curso_2(self):
        self.ID_CURSO = 2
        self.NOME_CURSO = 'CIÊNCIA DE COMPUTAÇÃO'
        self.HORAS = 64
        self.PERIODOS = 8
        self.DISCIPLINA_POR_PERIODO = 8
        self.TOTAL_DISCIPLINA = self.PERIODOS * self.DISCIPLINA_POR_PERIODO
        self.QTD_ALUNOS = 62

        return {'ID_CURSO': self.ID_CURSO,
                'NOME_CURSO': self.NOME_CURSO,
                'HORAS': self.HORAS,
                'PERIODOS': self.PERIODOS,
                'DISCIPLINA_POR_PERIODO': self.DISCIPLINA_POR_PERIODO,
                'TOTAL_DISCIPLINA': self.TOTAL_DISCIPLINA,
                'QTD_ALUNOS': self.QTD_ALUNOS}

    def get_curso_3(self):
        self.ID_CURSO = 3
        self.NOME_CURSO = 'SISTEMA DE INFORMAÇÕES'
        self.HORAS = 64
        self.PERIODOS = 8
        self.DISCIPLINA_POR_PERIODO = 7
        self.TOTAL_DISCIPLINA = self.PERIODOS * self.DISCIPLINA_POR_PERIODO
        self.QTD_ALUNOS = 48

        return {'ID_CURSO': self.ID_CURSO,
                'NOME_CURSO': self.NOME_CURSO,
                'HORAS': self.HORAS,
                'PERIODOS': self.PERIODOS,
                'DISCIPLINA_POR_PERIODO': self.DISCIPLINA_POR_PERIODO,
                'TOTAL_DISCIPLINA': self.TOTAL_DISCIPLINA,
                'QTD_ALUNOS': self.QTD_ALUNOS}

    def get_curso_4(self):
        self.ID_CURSO = 4
        self.NOME_CURSO = 'JOGOS DIGITAIS'
        self.HORAS = 48
        self.PERIODOS = 6
        self.DISCIPLINA_POR_PERIODO = 6
        self.TOTAL_DISCIPLINA = self.PERIODOS * self.DISCIPLINA_POR_PERIODO
        self.QTD_ALUNOS = 32

        return {'ID_CURSO': self.ID_CURSO,
                'NOME_CURSO': self.NOME_CURSO,
                'HORAS': self.HORAS,
                'PERIODOS': self.PERIODOS,
                'DISCIPLINA_POR_PERIODO': self.DISCIPLINA_POR_PERIODO,
                'TOTAL_DISCIPLINA': self.TOTAL_DISCIPLINA,
                'QTD_ALUNOS': self.QTD_ALUNOS}

    def get_curso_5(self):
        self.ID_CURSO = 5
        self.NOME_CURSO = 'TECNÓLOGO EM REDES DIGITAIS'
        self.HORAS = 48
        self.PERIODOS = 4
        self.DISCIPLINA_POR_PERIODO = 6
        self.TOTAL_DISCIPLINA = self.PERIODOS * self.DISCIPLINA_POR_PERIODO
        self.QTD_ALUNOS = 28

        return {'ID_CURSO': self.ID_CURSO,
                'NOME_CURSO': self.NOME_CURSO,
                'HORAS': self.HORAS,
                'PERIODOS': self.PERIODOS,
                'DISCIPLINA_POR_PERIODO': self.DISCIPLINA_POR_PERIODO,
                'TOTAL_DISCIPLINA': self.TOTAL_DISCIPLINA,
                'QTD_ALUNOS': self.QTD_ALUNOS}

    def salvar_cursos_csv(self):
        # Escrevendo em novo aquivo somente com os titulos das colunas
        with open('data/cursos.csv', 'w', encoding='UTF-8') as arq:
            lin = 'ID_CURSO;NOME_CURSO;HORAS;PERIODOS;DISCIPLINA_POR_PERIODO;TOTAL_DISCIPLINA;QTD_ALUNOS\n'
            arq.writelines(lin)

        with open('data/cursos.csv', 'a', encoding='UTF-8') as arq:

            c1 = self.get_curso_1()
            lin1 = f"{c1['ID_CURSO']};{c1['NOME_CURSO']};{c1['HORAS']};{c1['PERIODOS']};{
                c1['DISCIPLINA_POR_PERIODO']};{c1['TOTAL_DISCIPLINA']};{c1['QTD_ALUNOS']}\n"

            c2 = self.get_curso_2()
            lin2 = f"{c2['ID_CURSO']};{c2['NOME_CURSO']};{c2['HORAS']};{c2['PERIODOS']};{
                c2['DISCIPLINA_POR_PERIODO']};{c2['TOTAL_DISCIPLINA']};{c2['QTD_ALUNOS']}\n"

            c3 = self.get_curso_3()
            lin3 = f"{c3['ID_CURSO']};{c3['NOME_CURSO']};{c3['HORAS']};{c3['PERIODOS']};{
                c3['DISCIPLINA_POR_PERIODO']};{c3['TOTAL_DISCIPLINA']};{c3['QTD_ALUNOS']}\n"

            c4 = self.get_curso_4()
            lin4 = f"{c4['ID_CURSO']};{c4['NOME_CURSO']};{c4['HORAS']};{c4['PERIODOS']};{
                c4['DISCIPLINA_POR_PERIODO']};{c4['TOTAL_DISCIPLINA']};{c4['QTD_ALUNOS']}\n"

            c5 = self.get_curso_5()
            lin5 = f"{c5['ID_CURSO']};{c5['NOME_CURSO']};{c5['HORAS']};{c5['PERIODOS']};{
                c5['DISCIPLINA_POR_PERIODO']};{c5['TOTAL_DISCIPLINA']};{c5['QTD_ALUNOS']}\n"

            arq.writelines([lin1, lin2, lin3, lin4, lin5])
