import pandas as pd
import random


class Disciplina:

    def __init__(self) -> None:

        self.path = r"C:\Users\renato.vinicius\Documents\Python\Trabalho Pratico PUC\projeto_integracao\data\depara.xlsx"

        self.NOTA_CORTE = 70
        self.FREQ_MINIMA = 0.75
        self.lista_TIPO = ["TEORICA", "PRATICA"]

    def get_disciplinas_df(self):

        df = pd.read_excel(self.path, sheet_name='disciplinas')

        df['NOTA_CORTE'] = self.NOTA_CORTE

        df['FREQ_MINIMA'] = self.FREQ_MINIMA

        df['CARGA_HORARIA'] = ''

        df['TIPO'] = [random.choices(self.lista_TIPO, weights=[90, 10], k=1)[
            0] for i in range(df.shape[0])]

        return df

    def salvar_disciplinas_df(self):

        df = self.get_disciplinas_df()

        df.to_csv('data/disciplinas.csv', index=False, encoding='UTF-8')
