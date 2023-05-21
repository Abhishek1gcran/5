def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursive call to sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    sorted_arr = merge(left_half, right_half)
    return sorted_arr


def merge(left, right):
    merged = []
    left_idx = right_idx = 0
    
    # Compare elements from both lists and add the smaller one to the merged list
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    
    # Add any remaining elements from the left or right list
    while left_idx < len(left):
        merged.append(left[left_idx])
        left_idx += 1
    
    while right_idx < len(right):
        merged.append(right[right_idx])
        right_idx += 1
    
    return merged

# Example usage:
my_array = [5, 2, 9, 1, 7, 6, 3]
sorted_array = merge_sort(my_array)
print(sorted_array)
