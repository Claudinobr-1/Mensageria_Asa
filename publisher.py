import pika
import uuid
import json

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters=parameters)
channel = connection.channel()

channel.queue_declare(queue='UFU')

pedido_id = uuid.uuid4().hex
produto = input("Digite o produto: ")
quantidade = input("Digite a quantidade: ")

if not produto or not quantidade.isdigit():
    print("Produto inválido ou quantidade não é um número.")
    connection.close()
    exit(1)
 
dado_pedido = {
    "id": pedido_id,
    "produto": produto,
    "quantidade": quantidade,
    "status": "enviado_almoxarifado"
}

channel.basic_publish(
    exchange='', 
    routing_key='UFU', 
    body=json.dumps(dado_pedido).encode('utf-8')
)

print(f" [x] Pedido enviado: {json.dumps(dado_pedido)}")
connection.close()