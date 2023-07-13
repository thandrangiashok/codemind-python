# Read the matrix size
n, m = map(int, input().split())

# Initialize the maximum sum to 0
max_sum = 0

# Iterate over each row of the matrix
for _ in range(n):
    row = list(map(int, input().split()))
    row_sum = sum(row)
    max_sum = max(max_sum, row_sum)

# Print the maximum sum
print(max_sum)
