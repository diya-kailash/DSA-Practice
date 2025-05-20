# Quick Sort
# Time Complexity: O(n log n) 
# Space Complexity: O(log n) 

def partition(arr, low, high):
    i = low
    j = high
    pivot = arr[low]
    while i < j:
        while arr[i] <= pivot and i < high:
            i += 1
        while arr[j] > pivot and j > low:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[low] = arr[low], arr[j]
    return j
def quick_sort(arr, low, high):
    if low >= high:
        return
    p = partition(arr, low, high)
    quick_sort(arr, low, p-1)
    quick_sort(arr, p+1, high)  

arr = [13, 46, 24, 52, 20, 9, 1]
quick_sort(arr, 0, len(arr)-1)
print(*arr) 