def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

# Example usage:
my_array = [1, 3, 5, 7, 9, 11, 13]
target_value = 7
result = binary_search(my_array, target_value)
if result != -1:
    print(f"Element {target_value} found at index {result}")
else:
    print("Element not found")
