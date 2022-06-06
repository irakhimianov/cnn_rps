import random
from models import RPS, RPS_EMOJI


def get_result():
    num = random.randint(0, 2)
    return [RPS[num], RPS_EMOJI.get(num, 0)]