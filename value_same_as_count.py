def count_elements_with_condition(arr):
    count_dict = {}
    count = 0
    
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    for num, freq in count_dict.items():
        if num == freq:
            count += 1
    
    return count

# Read input
N = int(input())
arr = list(map(int, input().split()))

# Count elements satisfying the condition
result = count_elements_with_condition(arr)

# Display the result
print(result)
