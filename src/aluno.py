import random
from faker import Faker
from datetime import datetime
import pandas as pd

fake = Faker('pt_BR')


class Aluno:

    matriculas = []

    def __init__(self) -> None:

        self.path = r"C:\Users\renato.vinicius\Documents\Python\Trabalho Pratico PUC\projeto_integracao\data\alunos.csv"

        self.id_aluno = random.randint(1000, 999999)

        self.nome = None

        self.sexo = None

        self.registro_geral = None

        self.data_nascimento = None

        self.email = None

        self.telefone = None

        self.endereco = None

        self.status_matricula = None

        self.gerar_aluno()


    def gerar_aluno(self):

        self.id_aluno = random.randint(1000, 999999)

        if self.id_aluno not in Aluno.matriculas:

            Aluno.matriculas.append(self.id_aluno)

            # Gera nome completo com sexo aleatório
            sexo = random.choice(['Masculino', 'Feminino'])

            last_name = fake.last_name()

            if sexo == 'Masculino':

                first_name = fake.first_name_male()

                self.nome = f"{first_name} {last_name}"

                self.sexo = 'M'

            else:

                first_name = fake.first_name_female()

                self.nome = f"{first_name} {last_name}"

                self.sexo = 'F'

            self.endereco = fake.address()

            self.registro_geral = fake.cpf()

            start_date = datetime.strptime('1950-01-01', '%Y-%m-%d').date()

            end_date = datetime.strptime('1996-01-01', '%Y-%m-%d').date()

            self.data_nascimento = fake.date_between(
                start_date=start_date, end_date=end_date)

            self.email = f'{first_name.lower()}.{
                last_name.lower().replace(' ', '')}@trabalhopuc.br'

            self.telefone = fake.phone_number()

            self.endereco = fake.address().replace('\n', ' ')

            self.status_matricula = random.choice(
                ['Ativo', 'Trancado', 'Cancelado'])

    def gerar_alunos_df(self, qtd_alunos):

        lista_alunos = []

        col = ["ID_ALUNO", "NOME", "SEXO", "RG", "DATA_NASC", "EMAIL",
               "TELEFONE", "ENDERECO"]

        for i in range(qtd_alunos):

            aluno = Aluno()

            lista_alunos.append([aluno.id_aluno, aluno.nome, aluno.sexo,
                                 aluno.registro_geral, aluno.data_nascimento,
                                 aluno.email, aluno.telefone, aluno.endereco])

        df = pd.DataFrame(lista_alunos, columns=col)

        return df

    def gerar_alunos_csv(self, qtd_alunos):

        # Escrevendo em novo aquivo somente com os titulos das colunas
        with open('data/alunos.csv', 'w', encoding='UTF-8') as arq:
            lin = "ID_ALUNO;NOME;SEXO;RG;DATA_NASC;EMAIL;TELEFONE;ENDERECO\n"
            arq.writelines(lin)

        with open('data/alunos.csv', 'a', encoding='UTF-8') as arq:

            for i in range(qtd_alunos):

                aluno = Aluno()

                lin = f"{aluno.id_aluno};{aluno.nome};{aluno.sexo};{aluno.registro_geral};{
                    aluno.data_nascimento};{aluno.email};{aluno.telefone};{aluno.endereco}\n"

                arq.writelines(lin)

    def get_aluno_csv_gerado(self) -> pd.DataFrame:

        df = pd.read_csv(self.path, sep=';')

        return df
