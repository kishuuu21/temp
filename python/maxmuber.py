def find_max(arr):
    if not arr:
        return None  # Handle empty list
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

arr = [5, 7, 1, 12, 2, 3, 4]
maximum = find_max(arr)
print("Maximum number is:", maximum)
