def count_elements_not_divisible(arr, K):
    count = 0

    # Check each element in the array
    for num in arr:
        if num % K != 0:
            count += 1

    return count

# Read input
N, K = map(int, input().split())
arr = list(map(int, input().split()))

# Get the count of elements not divisible by K
result = count_elements_not_divisible(arr, K)

# Print the result
print(result)
