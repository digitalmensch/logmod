import logmod
import secrets
import random

logmod.logmod(secrets, random)

def coolname():
    return secrets.token_hex(5)

name = coolname()
print(f'Hello, {name}')
print(random.random())
