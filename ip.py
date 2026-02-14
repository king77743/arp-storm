import random
def get_random_ip():

    ip=[f"{random.randint(0,255)}" for _ in range(4)]
    return ".".join(ip)

