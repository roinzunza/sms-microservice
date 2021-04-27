
# sms-microservice

SMS Microservice using Python, Twilio and Redis Pub/Sub. Main service will send a SMS message using Twilio. The second service (pub) will send the data pertaining to the (sub) main service.

## Acknowledgements

 - [twilio blog reference](https://www.twilio.com/blog/sms-microservice-python-twilio-redis-pub-sub)
 - [Awesome Read on Redis](https://www.tutorialspoint.com/redis/redis_pub_sub.htm)
 - [How to setup Redis](https://www.devglan.com/blog/install-redis-windows-and-mac)


## Variables

To run this project, you will need to add the following variables.

`TWILIO_ACCOUNT_SID`
`TWILIO_AUTH_TOKEN`
`TWILIO_NUMBER`


## Run Locally

Clone the project

```bash
  git clone https://github.com/roinzunza/sms-microservice.git
```

Go to the project directory

```bash
  cd sms-microservice
```

Install dependencies
- create virtual env first.

```bash
  pip install -r requirements.txt
```

Start the Redis server

```bash
  redis-server
```
Open up two more terminals and activate your venv again per terminal

```bash 2
  python sub.py
```

```bash 3
  python pub.py
```
