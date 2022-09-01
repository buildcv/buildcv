import random 
import string



def create_random_string():
    random_str = ''.join(random.choice(string.ascii_letters) for i in range(6))
    return '_rand_' + random_str



