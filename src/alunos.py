from typing import Literal


class Alunos:

    # i.	Matrícula (número aleatório)
    # ii.	Nome (Nome e sobrenome)
    # iii.	Sexo (M | F)
    # iv.	Cadastro geral da pessoa (um código único, similar ao CPF)
    # v.	Data de nascimento (dd/mm/aaaa)
    # vi.	E-mail para contato (nome.sobrenome@trabalhopuc.br)
    # vii.	Endereço (pode ser cidade e estado)
    # viii.	Telefone celular (+55 XX XXXXX-XXXX)
    # ix.	Curso (código do curso)
    # x.	Data de ingresso (dd/mm/aaaa)
    # xi.	Data prevista de conclusão (dd/mm/aaaa)
    # xii.	Data de conclusão (dd/mm/aaaa)
    # xiii.	Status da matrícula (ativo | Trancado | Cancelado)

    def __init__(self,  matricula: str,
                 nome: str,
                 sexo: Literal['M', 'F'],
                 cadastro_geral: str,
                 data_nascimento: str,
                 email: str,
                 telefone: str,
                 endereco: str,
                 curso: str,
                 data_ingresso: str,
                 data_prevista_conclusao: str,
                 data_conclusao: str,
                 status_matricula: Literal['Ativo', 'Trancado', 'Cancelado']) -> None:

        self.matricula = matricula

        self.nome = nome

        self.sexo = sexo

        self.cadastro_geral = cadastro_geral

        self.data_nascimento = data_nascimento

        self.email = email

        self.telefone = telefone

        self.endereco = endereco

        self.curso = curso

        self.data_ingresso = data_ingresso

        self.data_prevista_conclusao = data_prevista_conclusao

        self.data_conclusao = data_conclusao

        self.status_matricula = status_matricula
