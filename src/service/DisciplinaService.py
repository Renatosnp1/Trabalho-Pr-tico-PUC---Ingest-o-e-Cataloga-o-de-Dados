class DisciplinaService:
    def __init__(self, disciplinas):
        self.disciplinas = disciplinas

    def top_10_maior_reprovacao(self):
        disciplinas_ordenadas = sorted(self.disciplinas, key=lambda disciplina: disciplina.reprovados, reverse=True)
        return disciplinas_ordenadas[:10]

    def top_10_menor_reprovacao(self):
        disciplinas_ordenadas = sorted(self.disciplinas, key=lambda disciplina: disciplina.reprovados)
        return disciplinas_ordenadas[:10]

    def maior_percentual_notas_acima_media(self):
        return max(self.disciplinas, key=lambda disciplina: disciplina.percentual_notas_acima_media)

    def menor_percentual_notas_acima_media(self):
        return min(self.disciplinas, key=lambda disciplina: disciplina.percentual_notas_acima_media)

    def maior_percentual_notas_abaixo_media(self):
        return max(self.disciplinas, key=lambda disciplina: disciplina.percentual_notas_abaixo_media)

    def menor_percentual_notas_abaixo_media(self):
        return min(self.disciplinas, key=lambda disciplina: disciplina.percentual_notas_abaixo_media)
