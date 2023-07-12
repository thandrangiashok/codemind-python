def count_sorted_columns(matrixA):
    rows = len(matrixA)
    columns = len(matrixA[0])
    count = 0

    for col in range(columns):
        is_sorted = True
        for row in range(1, rows):
            if matrixA[row][col] < matrixA[row-1][col]:
                is_sorted = False
                break
        if is_sorted:
            count += 1

    return count

# Read input
N, M = map(int, input().split())
matrixA = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrixA.append(row)

# Call the function and print the result
result = count_sorted_columns(matrixA)
print(result)