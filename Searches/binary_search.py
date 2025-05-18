# Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

# Iterative Approach
def binary_search(arr, key):
    low, high = 0, len(arr)-1
    while(low <= high):
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid +1
        else:
            high = mid -1
    return -1    

# Recursive Approach
def binary_search_recur(arr, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binary_search_recur(arr, key, mid + 1, high)
    else:
        return binary_search_recur(arr, key, low, mid - 1)
    
arr = [25, 32, 46, 75, 98, 102, 157]
x = binary_search(arr, 98)
y = binary_search_recur(arr, 25, 0, len(arr)-1)
print(x, y)