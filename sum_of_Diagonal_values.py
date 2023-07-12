def sum_diagonal_values(matrixA):
    rows = len(matrixA)
    columns = len(matrixA[0])
    diagonal_sum = 0

    for i in range(min(rows, columns)):
        diagonal_sum += matrixA[i][i]  # Add main diagonal value
        if i != rows - i - 1:  # Exclude the center element
            diagonal_sum += matrixA[i][rows - i - 1]  # Add anti-diagonal value

    return diagonal_sum

# Read input
N, M = map(int, input().split())
matrixA = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrixA.append(row)

# Call the function and print the result
result = sum_diagonal_values(matrixA)
print(result)