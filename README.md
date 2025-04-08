# Sistema de Mensageria com RabbitMQ

Este projeto implementa um sistema de mensageria utilizando RabbitMQ. Ele é composto por dois scripts principais: `publisher.py` e `consumer.py`. O objetivo é simular o envio e processamento de pedidos em um sistema de almoxarifado.

## Requisitos

- Python 3.x
- RabbitMQ instalado e em execução na máquina local
- Biblioteca `pika` instalada (`pip install pika`)

## Estrutura do Projeto

- **`publisher.py`**: Responsável por enviar mensagens (pedidos) para a fila RabbitMQ.
- **`consumer.py`**: Responsável por consumir as mensagens da fila, processá-las e enviá-las para outra fila.

## Funcionamento

### Publisher (`publisher.py`)

1. O script solicita ao usuário que insira:
   - O nome do produto.
   - A quantidade desejada.
2. Gera um identificador único para o pedido.
3. Cria uma mensagem no formato JSON com os seguintes campos:
   - `id`: Identificador único do pedido.
   - `produto`: Nome do produto.
   - `quantidade`: Quantidade solicitada.
   - `status`: Status inicial do pedido (`enviado_almoxarifado`).
4. Publica a mensagem na fila `UFU` do RabbitMQ.
5. Exibe no console a mensagem enviada.

### Consumer (`consumer.py`)

1. O script consome mensagens da fila `UFU`.
2. Ao receber uma mensagem:
   - Decodifica o conteúdo da mensagem.
   - Atualiza o status do pedido para `processado_almoxarifado`.
3. Publica a mensagem atualizada na fila `almoxarifado_processado`.
4. Exibe no console a mensagem processada.

### Fluxo de Mensagens

1. O `publisher.py` envia mensagens para a fila `UFU`.
2. O `consumer.py` consome as mensagens da fila `UFU`, processa os pedidos e os envia para a fila `almoxarifado_processado`.

## Como Executar

### Passo 1: Configurar o RabbitMQ

Certifique-se de que o RabbitMQ está instalado e em execução na máquina local. Use as credenciais padrão (`guest`/`guest`).

### Passo 2: Executar o Publisher

1. Abra um terminal.
2. Execute o comando:
   python publisher.py

### Passo 3: Executar o Consumer

1. Abra um novo terminal.
2. Execute o comando:
   python consumer.py