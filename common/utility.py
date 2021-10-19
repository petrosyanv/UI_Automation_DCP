import string
import random


def email_generator(length=8, digits=False):
    symbols = string.ascii_lowercase + string.digits if digits is True else string.ascii_lowercase
    email = ''.join([random.choice(symbols) for _ in range(length)]) + '@reqres.com'
    return email