from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('topico-alunos',
                         bootstrap_servers='localhost:9092',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for mensagem in consumer:
    print(f"Recebido: {mensagem.value}")
