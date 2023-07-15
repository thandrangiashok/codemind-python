def find_max_min_with_condition(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    max_val = float('-inf')
    min_val = float('inf')
    
    for num, count in count_dict.items():
        if num == count:
            max_val = max(max_val, num)
            min_val = min(min_val, num)
    
    if max_val == float('-inf') or min_val == float('inf'):
        return -1
    else:
        return min_val, max_val

# Read input
N = int(input())
arr = list(map(int, input().split()))

# Find max and min satisfying the condition
result = find_max_min_with_condition(arr)

# Display the result
if result == -1:
    print(-1)
else:
    min_val, max_val = result
    print(min_val, max_val)
