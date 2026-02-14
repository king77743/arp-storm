import random
def mac():
    gen=[f"{random.randint(0,255):02x}" for _ in range(6)]
    return ":".join(gen).upper()
