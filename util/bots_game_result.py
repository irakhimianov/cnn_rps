import random
from models import RPS


def get_result():
    return RPS[random.randint(0, 2)]