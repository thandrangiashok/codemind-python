N, M = map(int, input().split())

matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

column_sums = [0] * M
for row in matrix:
    for j in range(M):
        column_sums[j] += row[j]

print(" ".join(map(str, column_sums)))
