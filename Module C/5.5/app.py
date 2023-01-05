import redis
import json

red = redis.Redis(
    host='redis-10559.c135.eu-central-1-1.ec2.cloud.redislabs.com',
    port=10559,
    password='YXvE0hOlNWOnNDhNLyqlaJ3wLAXf4EiW'
)

cont = True

while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:\t')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break