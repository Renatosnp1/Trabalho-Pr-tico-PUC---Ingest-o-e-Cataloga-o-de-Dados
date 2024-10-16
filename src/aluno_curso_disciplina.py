from typing import Literal
from src.cursos import Curso
from src.disciplina import Disciplina
from src.aluno import Aluno
import pandas as pd
import random
import os


class CriandoTurmas:

    # alunos_turma = []

    def __init__(self) -> None:

        self.aluno = Aluno()

        self.curso = Curso()

        self.path = r"C:\Users\renato.vinicius\Documents\Python\Trabalho Pratico PUC\projeto_integracao\data\depara.xlsx"

        self.alunos_turma = []

    def get_depara_turma(self, id_curso: int):

        df = pd.read_excel(self.path, sheet_name='alunos_cursos_disciplinas')

        df = df[df['ID_CURSO'] == id_curso]

        return df

    # Criando um turma com alunos aleatórios
    def gerar_turma_curso_1(self):

        curso = self.curso.get_curso_1()

        molde_turma = self.get_depara_turma(id_curso=1)

        df1 = pd.DataFrame()

        # Criando mais turmas
        for turma in range(1, 10):

            aluno = Aluno()

            alunos = aluno.gerar_alunos_df(qtd_alunos=curso['QTD_ALUNOS'])

            for id_aluno in alunos['ID_ALUNO']:

                molde_turma['TURMA'] = turma

                molde_turma['ID_ALUNO'] = id_aluno

                # Organizando a quantidade de matérias por periodo
                molde_turma['PERIODO'] = [i for i in range(
                    1, curso['PERIODOS']+1) for y in range(curso['DISCIPLINA_POR_PERIODO'])]

                # Gerando frequência de forma aleatória
                molde_turma['FREQ_ALUNO'] = [random.randint(
                    70, 100)/100 for i in range(curso['TOTAL_DISCIPLINA'])]

                molde_turma['DATA_INGRESSO_CURSO'] = f'01/02/20{15+turma}'

                molde_turma['DATA_PREVISTA_CONCLUSAO'] = f'20/11/20{18+turma}'

                df1 = pd.concat([df1, molde_turma])

        df1 = df1.drop_duplicates(
            subset=['ID_CURSO', 'ID_DISCIPLINA', 'ID_ALUNO'])

        if os.path.isfile('data/turmas.csv'):

            df = pd.read_csv('data/turmas.csv', encoding='UTF-8')

            df1 = pd.concat([df1, df])

            df1.to_csv('data/turmas.csv', index=False, encoding='UTF-8')

        else:

            df1.to_csv('data/turmas.csv', index=False, encoding='UTF-8')

    def gerar_turma_curso_2(self):

        curso = self.curso.get_curso_2()

        molde_turma = self.get_depara_turma(id_curso=2)

        df1 = pd.DataFrame()

        # Criando mais turmas
        for turma in range(1, 10):

            aluno = Aluno()

            alunos = aluno.gerar_alunos_df(qtd_alunos=curso['QTD_ALUNOS'])

            for id_aluno in alunos['ID_ALUNO']:

                molde_turma['TURMA'] = turma

                molde_turma['ID_ALUNO'] = id_aluno

                # Organizando a quantidade de matérias por periodo
                molde_turma['PERIODO'] = [i for i in range(
                    1, curso['PERIODOS']+1) for y in range(curso['DISCIPLINA_POR_PERIODO'])]

                # Gerando frequência de forma aleatória
                molde_turma['FREQ_ALUNO'] = [random.randint(
                    70, 100)/100 for i in range(curso['TOTAL_DISCIPLINA'])]

                molde_turma['DATA_INGRESSO_CURSO'] = f'01/02/20{23+turma}'

                molde_turma['DATA_PREVISTA_CONCLUSAO'] = f'20/11/20{27+turma}'

                df1 = pd.concat([df1, molde_turma])

        df1 = df1.drop_duplicates(
            subset=['ID_CURSO', 'ID_DISCIPLINA', 'ID_ALUNO'])

        if os.path.isfile('data/turmas.csv'):

            df = pd.read_csv('data/turmas.csv', encoding='UTF-8')

            df1 = pd.concat([df1, df])

            df1.to_csv('data/turmas.csv', index=False, encoding='UTF-8')

        else:

            df1.to_csv('data/turmas.csv', index=False, encoding='UTF-8')

    def gerar_turma_curso_3(self):

        curso = self.curso.get_curso_3()

        molde_turma = self.get_depara_turma(id_curso=3)

        df1 = pd.DataFrame()

        # Criando mais turmas
        for turma in range(1, 10):

            aluno = Aluno()

            alunos = aluno.gerar_alunos_df(qtd_alunos=curso['QTD_ALUNOS'])

            for id_aluno in alunos['ID_ALUNO']:

                molde_turma['TURMA'] = turma

                molde_turma['ID_ALUNO'] = id_aluno

                # Organizando a quantidade de matérias por periodo
                molde_turma['PERIODO'] = [i for i in range(
                    1, curso['PERIODOS']+1) for y in range(curso['DISCIPLINA_POR_PERIODO'])]

                # Gerando frequência de forma aleatória
                molde_turma['FREQ_ALUNO'] = [random.randint(
                    70, 100)/100 for i in range(curso['TOTAL_DISCIPLINA'])]

                molde_turma['DATA_INGRESSO_CURSO'] = f'01/02/20{23+turma}'

                molde_turma['DATA_PREVISTA_CONCLUSAO'] = f'20/11/20{27+turma}'

                df1 = pd.concat([df1, molde_turma])

        df1 = df1.drop_duplicates(
            subset=['ID_CURSO', 'ID_DISCIPLINA', 'ID_ALUNO'])

        if os.path.isfile('data/turmas.csv'):

            df = pd.read_csv('data/turmas.csv', encoding='UTF-8')

            df1 = pd.concat([df1, df])

            df1.to_csv('data/turmas.csv', index=False, encoding='UTF-8')

        else:

            df1.to_csv('data/turmas.csv', index=False, encoding='UTF-8')

    def gerar_turma_curso_4(self):

        curso = self.curso.get_curso_4()

        molde_turma = self.get_depara_turma(id_curso=4)

        df1 = pd.DataFrame()

        # Criando mais turmas
        for turma in range(1, 10):

            aluno = Aluno()

            alunos = aluno.gerar_alunos_df(qtd_alunos=curso['QTD_ALUNOS'])

            for id_aluno in alunos['ID_ALUNO']:

                molde_turma['TURMA'] = turma

                molde_turma['ID_ALUNO'] = id_aluno

                # Organizando a quantidade de matérias por periodo
                molde_turma['PERIODO'] = [i for i in range(
                    1, curso['PERIODOS']+1) for y in range(curso['DISCIPLINA_POR_PERIODO'])]

                # Gerando frequência de forma aleatória
                molde_turma['FREQ_ALUNO'] = [random.randint(
                    70, 100)/100 for i in range(curso['TOTAL_DISCIPLINA'])]

                molde_turma['DATA_INGRESSO_CURSO'] = f'01/02/20{23+turma}'

                molde_turma['DATA_PREVISTA_CONCLUSAO'] = f'20/11/20{27+turma}'

                df1 = pd.concat([df1, molde_turma])

        df1 = df1.drop_duplicates(
            subset=['ID_CURSO', 'ID_DISCIPLINA', 'ID_ALUNO'])

        if os.path.isfile('data/turmas.csv'):

            df = pd.read_csv('data/turmas.csv', encoding='UTF-8')

            df1 = pd.concat([df1, df])

            df1.to_csv('data/turmas.csv', index=False, encoding='UTF-8')

        else:

            df1.to_csv('data/turmas.csv', index=False, encoding='UTF-8')

    def gerar_turma_curso_5(self):

        curso = self.curso.get_curso_5()

        molde_turma = self.get_depara_turma(id_curso=5)

        df1 = pd.DataFrame()

        # Criando mais turmas
        for turma in range(1, 10):

            aluno = Aluno()

            alunos = aluno.gerar_alunos_df(qtd_alunos=curso['QTD_ALUNOS'])

            for id_aluno in alunos['ID_ALUNO']:

                molde_turma['TURMA'] = turma

                molde_turma['ID_ALUNO'] = id_aluno

                # Organizando a quantidade de matérias por periodo
                molde_turma['PERIODO'] = [i for i in range(
                    1, curso['PERIODOS']+1) for y in range(curso['DISCIPLINA_POR_PERIODO'])]

                # Gerando frequência de forma aleatória
                molde_turma['FREQ_ALUNO'] = [random.randint(
                    70, 100)/100 for i in range(curso['TOTAL_DISCIPLINA'])]

                molde_turma['DATA_INGRESSO_CURSO'] = f'01/02/20{23+turma}'

                molde_turma['DATA_PREVISTA_CONCLUSAO'] = f'20/11/20{27+turma}'

                df1 = pd.concat([df1, molde_turma])

        df1 = df1.drop_duplicates(
            subset=['ID_CURSO', 'ID_DISCIPLINA', 'ID_ALUNO'])

        if os.path.isfile('data/turmas.csv'):

            df = pd.read_csv('data/turmas.csv', encoding='UTF-8')

            df1 = pd.concat([df1, df])

            df1.to_csv('data/turmas.csv', index=False, encoding='UTF-8')

        else:

            df1.to_csv('data/turmas.csv', index=False, encoding='UTF-8')
