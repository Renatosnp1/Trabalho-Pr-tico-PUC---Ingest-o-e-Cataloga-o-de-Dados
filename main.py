from src.atividade import Atividade
from src.cursos import Curso
from src.aluno import Aluno
from src.disciplina import Disciplina
from src.aluno_curso_disciplina import CriandoTurmas


aluno = Aluno()
aluno.gerar_alunos_csv(qtd_alunos=10_000)


curso = Curso()
curso.salvar_cursos_csv()

criandoturmas = CriandoTurmas()
criandoturmas.gerar_turma_curso_1()
criandoturmas.gerar_turma_curso_2()
criandoturmas.gerar_turma_curso_3()
criandoturmas.gerar_turma_curso_4()
criandoturmas.gerar_turma_curso_5()


disciplina = Disciplina()
disciplina.get_disciplinas_df()


atividade = Atividade()
atividade.criando_atividades_csv()
