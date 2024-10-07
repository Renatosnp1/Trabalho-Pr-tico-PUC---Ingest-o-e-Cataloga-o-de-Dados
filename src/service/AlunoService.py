from datetime import date
from typing import List, Dict

from src.aluno import Aluno


class AlunoService:
    def __init__(self, alunos: List[Aluno]):
        self.alunos = alunos

    def total_alunos_cadastrados(self) -> int:
        # Retorna o número total de alunos cadastrados
        return len(self.alunos)

    def total_alunos_unicos(self) -> int:
        # Usa registro geral para verificar a unicidade dos alunos
        registros_unicos = set([aluno.registro_geral for aluno in self.alunos])
        return len(registros_unicos)

    def faixa_etaria_notas(self) -> Dict[str, List]:
        # Retorna a faixa etária dos alunos que possuem notas altas e baixas
        notas_altas = []
        notas_baixas = []
        for aluno in self.alunos:
            idade = self.calcular_idade(aluno.data_nascimento)
            faixa_etaria = self.classificar_faixa_etaria(idade)
            # Verifica as notas do aluno para saber se são altas ou baixas
            if hasattr(aluno, 'nota') and aluno.nota is not None:
                if aluno.nota >= 70:  # Notas altas
                    notas_altas.append((aluno, faixa_etaria))
                else:
                    notas_baixas.append((aluno, faixa_etaria))

        return {
            'notas_altas': notas_altas,
            'notas_baixas': notas_baixas
        }

    def classificar_faixa_etaria(self, idade: int) -> str:
        # Classifica a faixa etária com base na idade
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

    def calcular_idade(self, data_nascimento) -> int:
        # Calcula a idade a partir da data de nascimento
        hoje = date.today()
        return hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

    def top_melhores_alunos(self, n: int = 10) -> List[Aluno]:
        # Retorna os top N melhores alunos com base na média das notas
        alunos_ordenados = sorted([aluno for aluno in self.alunos if hasattr(aluno, 'nota')], key=lambda aluno: aluno.nota, reverse=True)
        return alunos_ordenados[:n]

    def quantidade_reprovados_por_frequencia(self) -> int:
        # Retorna a quantidade de alunos reprovados por frequência
        return len([aluno for aluno in self.alunos if hasattr(aluno, 'motivo_reprovacao') and aluno.motivo_reprovacao == 'Frequencia'])

    def quantidade_reprovados_por_nota(self) -> int:
        # Retorna a quantidade de alunos reprovados por nota
        return len([aluno for aluno in self.alunos if hasattr(aluno, 'motivo_reprovacao') and aluno.motivo_reprovacao == 'Nota'])
