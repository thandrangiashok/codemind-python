def absolute_difference(n):
    sum_of_squares = 0
    square_of_sum = 0

    for i in range(1, n + 1):
        sum_of_squares += i**2
        square_of_sum += i

    square_of_sum = square_of_sum**2

    difference = abs(sum_of_squares - square_of_sum)
    return difference

# Example usage
n = int(input())
result = absolute_difference(n)
print(result)
