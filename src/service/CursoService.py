class CursoService:
    def __init__(self, cursos):
        self.cursos = cursos

    def media_aprovacao_por_curso(self):
        media_por_curso = {}
        for curso in self.cursos:
            aprovados = [aluno for aluno in curso.alunos if aluno.status == 'Aprovado']
            media_aprovacao = len(aprovados) / len(curso.alunos) * 100
            media_por_curso[curso.nome_curso] = media_aprovacao

        return media_por_curso

    def tempo_medio_conclusao(self):
        tempos_conclusao = []
        for curso in self.cursos:
            tempos_curso = [aluno.tempo_conclusao for aluno in curso.alunos if aluno.status == 'Concluido']
            if tempos_curso:
                tempo_medio = sum(tempos_curso) / len(tempos_curso)
                tempos_conclusao.append(tempo_medio)

        return sum(tempos_conclusao) / len(tempos_conclusao) if tempos_conclusao else 0

    def curso_com_maior_indice_aprovacao(self):
        media_por_curso = self.media_aprovacao_por_curso()
        return max(media_por_curso, key=media_por_curso.get)

    def curso_com_menor_indice_aprovacao(self):
        media_por_curso = self.media_aprovacao_por_curso()
        return min(media_por_curso, key=media_por_curso.get)
