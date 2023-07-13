import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Read the number of warriors killed on day 1 and day 2
n1 = int(input())
n2 = int(input())

# Calculate the sum of warriors killed on the first two days
total_killed = n1 + n2

# Find the minimum number of warriors to be killed on the third day
for i in range(1, total_killed + 1):
    if is_prime(total_killed + i):
        print(i)
        break
