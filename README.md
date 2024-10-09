# Projeto Prático - Ingestão e Catalogação de Dados

## Curso:
- **Pós-graduação em Engenharia de Dados**

<img src="src/img/puc.png"  height="165">

## Universidade:
- **PONTIFÍCIA UNIVERSIDADE CATÓLICA DE MINAS GERAIS - PUC MINAS**

## Disciplina:
- **Ingestão e Catalogação de Dados**

## Alunos:
- Renato Vionicius Carneiro
- Bruno Hachenburg
- Paulo Victor Sobrinho
- Pedro Henrique Ferreira

---

## Descrição do Problema

Uma universidade precisa coletar dados de seus alunos das diversas unidades e cursos para construir um sistema analítico que permita o armazenamento e análise em tempo real das notas de cada estudante. Esse sistema deve calcular médias e, futuramente, gerar previsões sobre as disciplinas para que a instituição consiga tomar decisões que ajudem a melhorar a eficiência e produtividade dos alunos.

### Dados Passados pela Empresa Contratante:

1. **Nome da Instituição**: FACULDADE PRODATA

2. **Dados dos Cursos Ofertados**:

    - **ENGENHARIA DE COMPUTAÇÃO**
        - Código do curso: 1
        - Períodos: 10
        - Carga horária prevista por disciplina: até 92 horas
        - Disciplinas por período: 8
        - Média de alunos por turma: 50

    - **CIÊNCIA DA COMPUTAÇÃO**
        - Código do curso: 2
        - Períodos: 8
        - Carga horária prevista por disciplina: até 64 horas
        - Disciplinas por período: 8
        - Média de alunos por turma: 62

    - **SISTEMA DE INFORMAÇÕES**
        - Código do curso: 3
        - Períodos: 8
        - Carga horária prevista por disciplina: até 64 horas
        - Disciplinas por período: 7
        - Média de alunos por turma: 48

    - **JOGOS DIGITAIS**
        - Código do curso: 4
        - Períodos: 6
        - Carga horária prevista por disciplina: até 48 horas
        - Disciplinas por período: 6
        - Média de alunos por turma: 32

    - **TECNÓLOGO EM REDES DIGITAIS**
        - Código do curso: 5
        - Períodos: 4
        - Carga horária prevista por disciplina: até 48 horas
        - Disciplinas por período: 6
        - Média de alunos por turma: 28

3. **Dados Necessários dos Alunos**:

    - Matrícula (número aleatório)
    - Nome (Nome e sobrenome)
    - Sexo (M | F)
    - Cadastro geral da pessoa (um código único, similar ao CPF)
    - Data de nascimento (dd/mm/aaaa)
    - E-mail para contato (nome.sobrenome@trabalhopuc.br)
    - Endereço (pode ser cidade e estado)
    - Telefone celular (+55 XX XXXXX-XXXX)
    - Curso (código do curso)
    - Data de ingresso (dd/mm/aaaa)
    - Data prevista de conclusão (dd/mm/aaaa)
    - Data de conclusão (dd/mm/aaaa)
    - Status da matrícula (ativo | Trancado | Cancelado)

4. **Dados das Disciplinas dos Cursos**:

    - Código da disciplina (deve iniciar em 1, não pode repetir).
    - Nome da disciplina (Sugestão: busque informações sobre os cursos fornecidos acima para que os dados sejam mais coesos).
    - Tipo: Teórica | prática
    - Nota de corte: 70 pontos
    - Carga horária prevista: Gerar um valor aleatório de acordo com a carga horária prevista por disciplina. O número deve ser SEMPRE maior que 16 horas e menor que a carga horária prevista por disciplina.
    - Frequência mínima (deve ser equivalente à 75% da carga horária)

5. **Dados de Relacionamento entre Alunos, Cursos e Disciplinas**:

    - Código do curso
    - Código da disciplina
    - Período (mm/aaaa)
    - Matrícula do aluno
    - Nota do aluno
    - Frequência do aluno
    - Status (aprovado | reprovado | exame especial)
    - Motivo reprovação (nota | frequência)

6. **Dados de Atividades Realizadas pelo Aluno**:

    - Matrícula do aluno
    - Código do curso
    - Código da disciplina
    - Período
    - Código da atividade (número sequencial de acordo com a atividade)
    - Nome da atividade (Exercício | Trabalho | Avaliação)
    - Valor da atividade
    - Nota obtida pelo aluno

### Considerações para o Desenvolvimento

- Um aluno não pode estar matriculado simultaneamente em mais de um curso, mas pode fazer mais de um curso (para cada ingresso, um novo código de matrícula deverá ser gerado).
- Um aluno não pode repetir o mesmo curso.
- Cada período deve conter entre 6 e 10 disciplinas (precisa estar nesse intervalo).
- A idade mínima para um aluno ingressar na universidade é a partir dos 18 anos.
- O aluno não pode trancar/cancelar uma disciplina, mas sim, o seu curso como um todo.
- A nota das atividades deve ser um valor inteiro. A soma do valor das atividades de cada disciplina não pode ultrapassar 100 pontos.
- O nome das atividades deve ser sucedido por X, onde X indica o código da atividade (exemplo: Atividade 1, Prova 2, Trabalho 3).

--- 

## Objetivo do Projeto

Criar um pipeline de ingestão e catalogação de dados que permita o armazenamento eficiente e análise em tempo real das notas e frequências dos alunos, possibilitando a construção de um sistema analítico para a instituição de ensino. O pipeline deve ser capaz de coletar, transformar e armazenar os dados de maneira estruturada, permitindo a criação de relatórios e visualizações para apoiar a tomada de decisão acadêmica e administrativa.

