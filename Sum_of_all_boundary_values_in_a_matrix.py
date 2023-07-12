def sum_boundary_values(matrixA):
    rows = len(matrixA)
    columns = len(matrixA[0])
    boundary_sum = 0

    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                boundary_sum += matrixA[i][j]

    return boundary_sum

# Read input
N, M = map(int, input().split())
matrixA = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrixA.append(row)

# Call the function and print the result
result = sum_boundary_values(matrixA)
print(result)