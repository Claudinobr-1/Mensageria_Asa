import pika, sys, os
import json

def callback(ch, method, properties, body):
    data = body.decode('utf-8')
    
    json_data = json.loads(data)
    
    json_data['status'] = 'processado_almoxarifado'

    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='almoxarifado_processado')
    channel.basic_publish(
        exchange='', 
        routing_key='almoxarifado_processado', 
        body=json.dumps(json_data).encode('utf-8')
    )
    print(f" [x] Pedido processado e enviado para a fila almoxarifado_processado: {json.dumps(json_data)}")
    connection.close()

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='UFU')

    channel.basic_consume(queue='UFU', on_message_callback=callback, auto_ack=True)

    print(' [*] Aguardando mensagens. CTRL+C para sair')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)