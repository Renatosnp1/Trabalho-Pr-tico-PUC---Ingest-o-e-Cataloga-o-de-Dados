from ..aluno import Aluno


def salvar_alunos_csv(aluno: Aluno):

    with open('src/database/alunos.csv', 'w', encoding='UTF-8') as arq:

        lin = f"{aluno.matricula};{aluno.nome};{aluno.sexo};{aluno.registro_geral}; \
            {aluno.data_nascimento};{aluno.email};{aluno.telefone};{aluno.endereco}"

        arq.writelines(lin)
