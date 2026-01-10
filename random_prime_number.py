
import random
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

while True:
    num = random.randint(2, 50)
    if is_prime(num):
        print(f"Found a prime number: {num}")
        break  
