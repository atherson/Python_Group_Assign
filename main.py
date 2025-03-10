import string
import random
def generate_password():
    host_word = string.ascii_uppercase + string.ascii_lowercase + string.ascii_letters + string.digits + string.punctuation 
    word = ''.join(random.choices(host_word, k=15))


def intro():
    print("1. Create a new account")
    print("2. Log in to an existing account")



