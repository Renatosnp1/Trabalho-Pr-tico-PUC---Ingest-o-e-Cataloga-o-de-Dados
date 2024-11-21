1. Desenho da Arquitetura do Ambiente

Será estruturado um Data Lake, denominado datalake-dados-faculdade, dividido em três camadas: raw, staging e dw. Todo o armazenamento será local, com os dados organizados em diferentes formatos:

Na Camada raw, os dados brutos serão armazenados em formatos como .json, .xml ou .csv, dependendo da fonte.
Na Camada staging, os dados serão transformados para formatos otimizados, como .parquet ou .delta, garantindo maior eficiência no processamento.
Na Camada dw, também serão utilizados os formatos .parquet ou .delta, facilitando consultas rápidas e análises.
Além disso, será utilizado um Banco de Dados Local (como PostgreSQL ou SQLite) para armazenar dados estruturados e prontos para consumo analítico.

A plataforma Dremio será usada como ferramenta de consulta analítica, mapeando e acessando as diferentes camadas do data lake. Para orquestrar as tarefas de ingestão, transformação e consumo de dados, o Apache Airflow será implementado. Já o Apache Kafka será utilizado para o processamento de fluxos de dados, permitindo a produção e o consumo de dados em tempo real.

2. Scripts de Automatização Padronizados

Serão criados scripts de automação, como os de ingestão e processamento de dados, padronizados com tags que identifiquem o ambiente, grupo e escopo da atividade. Esses scripts serão desenvolvidos em Python ou Bash e integrados ao Airflow e Kafka para garantir a automação e o gerenciamento eficiente das tarefas de ingestão e fluxo de dados.

