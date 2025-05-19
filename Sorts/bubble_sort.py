# Bubble Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(*arr)

arr = [13, 46, 24, 52, 20, 9, 1]
bubble_sort(arr)