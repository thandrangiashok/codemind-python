def find_pairs(arr):
    n = len(arr)
    pairs = []

    for i in range(n // 2):
        pairs.append((arr[i], arr[n - i - 1]))

    if n % 2 != 0:
        pairs.append((arr[n // 2], 0))

    return pairs

# Read input
N = int(input())
arr = list(map(int, input().split()))

# Find pairs of elements
result = find_pairs(arr)

# Display the result
for pair in result:
    print(pair[0], pair[1], end=" ")
