def sum_non_boundary_values(matrixA):
    rows = len(matrixA)
    columns = len(matrixA[0])
    non_boundary_sum = 0

    for i in range(rows):
        for j in range(columns):
            if i != 0 and i != rows - 1 and j != 0 and j != columns - 1:
                non_boundary_sum += matrixA[i][j]

    return non_boundary_sum

# Read input
N, M = map(int, input().split())
matrixA = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrixA.append(row)

# Call the function and print the result
result = sum_non_boundary_values(matrixA)
print(result)