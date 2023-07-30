from __future__ import absolute_import, unicode_literals

from .models import List

from celery import shared_task

import pika

def my_callback():
    print("aqui....")
    List.objects.create(text='asaddsad')

connection_params = pika.ConnectionParameters(
    host='127.0.0.1',
    port="5672",
    virtual_host='/',
    credentials=pika.PlainCredentials(
        username='guest', 
        password='guest'),
)

@shared_task
def consume_message():
    channel = pika.BlockingConnection(connection_params).channel()
    channel.queue_declare(queue='todo_list', durable=True)
    channel.basic_consume(
        queue='todo_list',
        auto_ack=True,
        on_message_callback=my_callback
    )