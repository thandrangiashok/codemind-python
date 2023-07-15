def count_unique_odd_elements(arr):
    unique_odd_set = set()
    
    for num in arr:
        if num % 2 != 0:
            unique_odd_set.add(num)
    
    return len(unique_odd_set)

# Read input
N = int(input())
arr = list(map(int, input().split()))

# Count unique odd elements
result = count_unique_odd_elements(arr)

# Display the result
print(result)
