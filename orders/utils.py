import random
import string

def generate_tracking_number():
    return "TRK-" + ''.join(random.choices(string.digits, k=8))
