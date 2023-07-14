def sum_of_digits(num):
    # Calculate the sum of digits in a number
    sum_digits = 0
    while num > 0:
        sum_digits += num % 10
        num //= 10
    return sum_digits

def sum_of_digits_in_array(arr):
    sum_total = 0
    # Iterate over each element in the array
    for num in arr:
        sum_total += sum_of_digits(num)
    return sum_total

# Read input
N = int(input())
arr = list(map(int, input().split()))

# Get the sum of digits of each element in the array
result = sum_of_digits_in_array(arr)

# Print the result
print(result)
