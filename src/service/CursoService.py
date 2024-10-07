from typing import List, Dict

from src.curso import Curso


class CursoService:
    def __init__(self, cursos: List[Curso]):
        self.cursos = cursos

    def media_aprovacao_por_curso(self) -> Dict[str, float]:
        media_por_curso = {}
        for curso in self.cursos:
            # Filtra os alunos aprovados
            aprovados = [aluno for aluno in curso.alunos if aluno.status == 'Aprovado']
            # Calcula a média de aprovação para o curso
            media_aprovacao = (len(aprovados) / len(curso.alunos)) * 100 if curso.alunos else 0
            media_por_curso[curso.nome_curso] = media_aprovacao

        return media_por_curso

    def tempo_medio_conclusao(self) -> float:
        tempos_conclusao = []
        for curso in self.cursos:
            # Filtra os tempos de conclusão dos alunos que concluíram o curso
            tempos_curso = [aluno.tempo_conclusao for aluno in curso.alunos if aluno.status == 'Concluido']
            if tempos_curso:
                # Calcula o tempo médio de conclusão para o curso
                tempo_medio = sum(tempos_curso) / len(tempos_curso)
                tempos_conclusao.append(tempo_medio)

        # Retorna o tempo médio total ou 0 se nenhum aluno concluiu o curso
        return sum(tempos_conclusao) / len(tempos_conclusao) if tempos_conclusao else 0

    def curso_com_maior_indice_aprovacao(self) -> str:
        media_por_curso = self.media_aprovacao_por_curso()
        # Retorna o nome do curso com a maior média de aprovação
        return max(media_por_curso, key=media_por_curso.get)

    def curso_com_menor_indice_aprovacao(self) -> str:
        media_por_curso = self.media_aprovacao_por_curso()
        # Retorna o nome do curso com a menor média de aprovação
        return min(media_por_curso, key=media_por_curso.get)
