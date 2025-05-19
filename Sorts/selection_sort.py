# Selection Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(*arr)

arr = [13, 46, 24, 52, 20, 9, 1]
selection_sort(arr)