from src.aluno import Aluno
from src.repository.repository import salvar_alunos_csv

for i in range(20):

    aluno = Aluno()

    salvar_alunos_csv(aluno)
    # print(aluno)
