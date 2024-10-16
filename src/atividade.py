import pandas as pd
import random


class Atividade:

    def __init__(self) -> None:

        pass

    def criando_atividades_csv(self):
        path = r'data\turmas.csv'

        cursos = pd.read_csv(path, encoding='UTF-8')

        cursos = cursos[['ID_CURSO', 'ID_DISCIPLINA', 'ID_ALUNO', 'PERIODO']]

        exercicio = cursos.copy()
        trabalho = cursos.copy()
        avaliacao = cursos.copy()

        exercicio['TIPO_ATIVIDADE'] = 'EXERCICIO'
        exercicio['NOTA'] = [random.randint(
            22, 30) for i in range(exercicio.shape[0])]

        trabalho['TIPO_ATIVIDADE'] = 'TRABALHO'
        trabalho['NOTA'] = [random.randint(
            22, 30) for i in range(trabalho.shape[0])]

        avaliacao['TIPO_ATIVIDADE'] = 'AVALIAÇÃO'
        avaliacao['NOTA'] = [random.randint(
            25, 40) for i in range(avaliacao.shape[0])]

        cursos1 = pd.concat([exercicio, trabalho, avaliacao])

        cursos1['ID_ATIVIDADE'] = 100000 + cursos1.index

        cursos1.to_csv('data/atividades.csv', index=False, encoding='UTF-8')
