from src.curso import Curso


eng_computacao = Curso(id_curso=1,
                       nome_curso='ENGENHARIA DE COMPUTAÇÃO',
                       periodo=10,
                       alunos_por_turma=50,
                       disciplica_por_periodo=8,
                       nota_corte=70,
                       carga_horaria_prevista=92)


cien_computacao = Curso(id_curso=2,
                        nome_curso='CIÊNCIA DA COMPUTAÇÃO',
                        periodo=8,
                        alunos_por_turma=62,
                        disciplica_por_periodo=8,
                        nota_corte=70,
                        carga_horaria_prevista=64)


siste_informacao = Curso(id_curso=3,
                         nome_curso='SISTEMA DE INFORMAÇÕES',
                         periodo=8,
                         alunos_por_turma=48,
                         disciplica_por_periodo=7,
                         nota_corte=70,
                         carga_horaria_prevista=64)


jogos_digit = Curso(id_curso=4,
                    nome_curso='JOGOS DIGITAIS',
                    periodo=6,
                    alunos_por_turma=32,
                    disciplica_por_periodo=6,
                    nota_corte=70,
                    carga_horaria_prevista=48)


tec_redes_digi = Curso(id_curso=5,
                       nome_curso='TECNÓLOGO EM REDES DIGITAIS',
                       periodo=4,
                       alunos_por_turma=28,
                       disciplica_por_periodo=6,
                       nota_corte=70,
                       carga_horaria_prevista=48)
