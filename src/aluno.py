import random
from faker import Faker
from datetime import datetime


fake = Faker('pt_BR')


class Aluno:

    def __init__(self) -> None:

        self.matricula = random.randint(1000, 999999)

        self.nome = None

        self.sexo = None

        self.registro_geral = None

        self.data_nascimento = None

        self.email = None

        self.telefone = None

        self.endereco = None

        self.gerar_aluno()
        # self.curso = curso
        # self.data_ingresso = data_ingresso
        # self.data_prevista_conclusao = data_prevista_conclusao
        # self.data_conclusao = data_conclusao

        self.status_matricula = random.choice(
            ['Ativo', 'Trancado', 'Cancelado'])

    def gerar_aluno(self):
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

        start_date = datetime.strptime('1970-01-01', '%Y-%m-%d').date()

        end_date = datetime.strptime('2020-01-01', '%Y-%m-%d').date()

        self.data_nascimento = fake.date_between(
            start_date=start_date, end_date=end_date)

        self.email = f'{first_name.lower()}.{last_name.lower()}@trabalhopuc.br'

        self.telefone = fake.phone_number()

        self.endereco = fake.address()

    def get_aluno(self):
        return {
            'MATRICULA': self.matricula,
            'NOME': self.nome,
            'SEXO': self.sexo,
            'RG': self.registro_geral,
            'DT_NASCIMENTO': self.data_nascimento,
            'EMAIL': self.email,
            'TELEFONE': self.telefone,
            'ENDERECO': self.endereco
        }

    def __str__(self) -> str:
        return f"""=====================================================
MATRICULA: {self.matricula}
NOME: {self.nome}
SEXO: {self.sexo}
RG: {self.registro_geral}
DT_NASCIMENTO: {self.data_nascimento}
EMAIL: {self.email}
TELEFONE: {self.telefone}
ENDERECO: {self.endereco}
====================================================="""
