from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

dados_aluno = {"matricula": 12345, "nome": "João", "curso": "Engenharia"}
producer.send('topico-alunos', dados_aluno)
