def odd_even_array(arr):
    odd = []
    even = []
    
    for num in arr:
        if num % 2 == 1:
            odd.append(num)
        else:
            even.append(num)
    
    return odd + even

# Read input
N = int(input())
arr = list(map(int, input().split()))

# Form odd-even array
result = odd_even_array(arr)

# Print the result
print(' '.join(map(str, result)))
