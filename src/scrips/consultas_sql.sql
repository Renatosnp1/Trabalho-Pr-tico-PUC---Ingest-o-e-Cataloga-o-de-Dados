SELECT COUNT(*) FROM alunos;


SELECT curso, AVG(aprovacao) FROM resultados GROUP BY curso;


SELECT disciplina, COUNT(*) AS reprovacoes FROM resultados WHERE status = 'Reprovado' GROUP BY disciplina ORDER BY reprovacoes DESC LIMIT 10;
