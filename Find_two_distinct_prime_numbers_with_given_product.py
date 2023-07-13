import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_product(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factor = n // i
            if is_prime(i) and is_prime(factor):
                return i, factor
    return -1

# Read the input
n = int(input())

# Find the prime product
result = find_prime_product(n)

# Print the result
if result == -1:
    print(-1)
else:
    print(result[0], result[1])
