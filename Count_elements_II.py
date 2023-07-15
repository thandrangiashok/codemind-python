def count_uncommon_elements(A, B):
    uncommon_elements = set(A) ^ set(B)
    return len(uncommon_elements)

# Read input
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Count uncommon elements
result = count_uncommon_elements(A, B)

# Display the result
print(result)
