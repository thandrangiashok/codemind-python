def even_odd_array(arr):
    even = []
    odd = []
    
    for num in arr:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    
    return even + odd

# Read input
N = int(input())
arr = list(map(int, input().split()))

# Form even-odd array
result = even_odd_array(arr)

# Print the result
print(' '.join(map(str, result)))
