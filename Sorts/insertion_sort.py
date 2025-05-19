# Insertion Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    print(*arr)
    
arr = [13, 46, 24, 52, 20, 9, 1]
insertion_sort(arr)