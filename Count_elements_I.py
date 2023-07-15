def count_common_elements(A, B):
    common_elements = set(A) & set(B)
    return len(common_elements)

# Read input
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Count common elements
result = count_common_elements(A, B)

# Display the result
print(result)
