import random


def code_generation():
    random.seed()
    return str(random.randint(10000, 99999))
