def sum_unique_elements(arr):
    unique_set = set(arr)
    return sum(unique_set)

# Read input
N = int(input())
arr = list(map(int, input().split()))

# Sum of unique elements
result = sum_unique_elements(arr)

# Display the result
print(result)
