from __future__ import absolute_import, unicode_literals

from celery import shared_task

import pika
import json

connection_params = pika.ConnectionParameters(
    host='localhost',
    port="5672",
    credentials=pika.PlainCredentials(
        username='guest',
        password='guest'),
)

@shared_task
def send_message(message):
    channel = pika.BlockingConnection(connection_params).channel()
    channel.basic_publish(
        body=json.dumps(message),
        exchange='users', 
        routing_key='', 
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )
    
    channel.close()