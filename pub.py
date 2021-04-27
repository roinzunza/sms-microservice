import os
import redis
import json

# pub file which is the link in which the message(s) will be transferred through the channel

# Redis connection
redis_conn = redis.Redis(charset="utf-8", decode_responses=True)

def pub():
    # json body of the message request for twilio
    data = {
        "message": "Test SMS!",
        "from": 'TWILIO_NUMBER',
        "to": "NUMBER_SENDING_TO"
    }

    # channel name = broadcast
    # dump json data to broadcast channel where subscriber picks up and processes the request
    redis_conn.publish("broadcast", json.dumps(data))

if __name__ == "__main__":
    pub()
