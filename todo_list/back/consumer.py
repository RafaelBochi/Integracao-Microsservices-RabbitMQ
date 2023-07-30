
import os
import django
import pika
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings') 
django.setup()


from todo_list.models import List
from usuario.models import Usuario
def my_callback(ch, method, properties, body):
    print("aqui....")
    data = json.loads(body)
    if data['type'] == 'create':
        Usuario.objects.create( username=data['username'] ,email=data['email'], password=data['password'])
    
    elif data['type'] == 'delete':
        Usuario.objects.get(email=data['email']).delete()
    

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()
channel.queue_declare(queue='todo_list', durable=True)

channel.basic_consume(queue='todo_list', on_message_callback=my_callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()