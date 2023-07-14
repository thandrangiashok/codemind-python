def is_palindrome(num):
    # Check if a number is a palindrome
    return str(num) == str(num)[::-1]

def count_palindromes_in_array(arr):
    count = 0
    # Iterate over each element in the array
    for num in arr:
        if is_palindrome(num):
            count += 1
    return count

# Read input
N = int(input())
arr = list(map(int, input().split()))

# Get the count of palindromes in the array
result = count_palindromes_in_array(arr)

# Print the result
print(result)
