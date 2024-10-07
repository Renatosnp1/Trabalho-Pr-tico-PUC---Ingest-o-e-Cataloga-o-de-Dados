class AlunoService:
    def __init__(self, alunos):
        self.alunos = alunos

    def total_alunos_cadastrados(self):
        # Retorna o número total de alunos cadastrados
        return len(self.alunos)

    def total_alunos_unicos(self):
        # Usa registro geral para verificar a unicidade dos alunos
        registros_unicos = set([aluno.registro_geral for aluno in self.alunos])
        return len(registros_unicos)

    def faixa_etaria_notas(self):
        # Retorna a faixa etária dos alunos que possuem notas altas e baixas
        notas_altas = []
        notas_baixas = []
        for aluno in self.alunos:
            idade = self.calcular_idade(aluno.data_nascimento)
            faixa_etaria = self.classificar_faixa_etaria(idade)
            # Aqui verificamos as notas do aluno para saber se são altas ou baixas
            if aluno.nota >= 70:  # Notas altas
                notas_altas.append((aluno, faixa_etaria))
            else:
                notas_baixas.append((aluno, faixa_etaria))

        return {
            'notas_altas': notas_altas,
            'notas_baixas': notas_baixas
        }

    def classificar_faixa_etaria(self, idade):
        if 18 <= idade <= 25:
            return "Pré-adulto"
        elif 26 <= idade <= 30:
            return "Jovem adulto I"
        elif 31 <= idade <= 35:
            return "Jovem adulto II"
        elif 36 <= idade <= 40:
            return "Adulto médio I"
        elif 41 <= idade <= 50:
            return "Adulto médio II"
        elif 51 <= idade <= 60:
            return "Adulto médio III"
        else:
            return "Adulto idoso"

    def calcular_idade(self, data_nascimento):
        from datetime import date
        hoje = date.today()
        return hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

    def top_melhores_alunos(self, n=10):
        # Retorna os top N melhores alunos com base na média das notas
        alunos_ordenados = sorted(self.alunos, key=lambda aluno: aluno.nota, reverse=True)
        return alunos_ordenados[:n]

    def quantidade_reprovados_por_frequencia(self):
        # Retorna a quantidade de alunos reprovados por frequência
        return len([aluno for aluno in self.alunos if aluno.motivo_reprovacao == 'Frequencia'])

    def quantidade_reprovados_por_nota(self):
        # Retorna a quantidade de alunos reprovados por nota
        return len([aluno for aluno in self.alunos if aluno.motivo_reprovacao == 'Nota'])
