# Linear Search
# Time Complexity: O(n)
# Space Complexity: O(1)

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = [21, 55, 73, 36, 0, 62, 88, 14, 97]
x = linear_search(arr, 62)
print(x)