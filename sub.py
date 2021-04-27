import redis
import json
import os

from twilio.rest import Client
from multiprocessing import Process

#redis connection
redis_conn = redis.Redis(charset="utf-8", decode_responses=True)


def sub(name: str):
    pubsub = redis_conn.pubsub()
    # channel name = broadcast
    pubsub.subscribe("broadcast")
    print('listening for channels...')
    for message in pubsub.listen():
        if message.get("type") == "message":
            data = json.loads(message.get("data"))
            print('{} : {}'.format(name, data))

            account_sid = 'TWILIO_ACCOUNT_SID'
            auth_token = 'TWILIO_AUTH_TOKEN'

            body = data.get("message")
            from_ = data.get("from")
            to = data.get("to")

            client = Client(account_sid, auth_token)
            message = client.messages.create(from_=from_, to=to, body=body)
            print("message id: {}".format(message.sid))
            # output:
            '''
            reader : {'message': 'Test SMS!', 'from': 'twilio_number', 'to': 'NUMBER_SENDING_TO'}
            message id: SM4757260f6e324e338385d90577f5ead3
            '''




if __name__ == "__main__":
    Process(target=sub, args=("reader",)).start()
