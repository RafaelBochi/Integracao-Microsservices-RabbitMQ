import os
import django
import pika
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings') 
django.setup()
from usuario.models import Usuario
def my_callback(ch, method, properties, body):
    print("aqui....")
    data = json.loads(body)
    print(data)
    print(data[0][0]['email'])
    if data[0][0]['type'] == 'create':
        Usuario.objects.create( username=data[0][0]['username'] ,email=data[0][0]['email'], password=data[0][0]['password'])
    
    elif data[0][0]['type'] == 'delete':
        Usuario.objects.get(email=data[0][0]['email']).delete()
    

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', heartbeat=600, blocked_connection_timeout=10000))
channel = connection.channel()
channel.queue_declare(queue='celery', durable=True)

channel.basic_consume(queue='celery', on_message_callback=my_callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()