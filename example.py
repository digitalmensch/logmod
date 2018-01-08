import secrets
import random
import logmod

logmod.logmod(secrets, random)

def cool_number(x):
    return random.random() * x * random.randint(0, x)

for i in range(10):
    print(i, random.random(), cool_number(i))


hex_name = secrets.token_hex(5)
print(f'Hello, {hex_name}')

