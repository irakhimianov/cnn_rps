import random
from models import RPS, RPS_EMOJI


def get_result():
    res = random.randint(0, 2)
    return [RPS[res], RPS_EMOJI.get(RPS[res], 0)]