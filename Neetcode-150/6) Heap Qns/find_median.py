# Find Median from Data Stream (Naive Implementation)
# Overall Time Complexity:
# - addNum: O(1)
# - findMedian: O(n log n)
# Overall Space Complexity: O(n)
# Hint: Store all numbers in a list and sort it when finding median

class MedianFinder:
    def __init__(self):
        self.nums = []                      

    def addNum(self, num: int) -> None:
        self.nums.append(num)             

    def findMedian(self) -> float:
        self.nums.sort()                    
        n = len(self.nums)
        return self.nums[n//2] if n % 2 != 0 else (self.nums[n//2] + self.nums[n//2 - 1]) / 2

# Time Complexity:
# - addNum: O(1) for appending to list
# - findMedian:
#   - Sorting list of n elements: O(n log n)
#   - Accessing middle elements: O(1)
#   - Total: O(n log n)
# Space Complexity:
# - List stores all numbers added: O(n)
# - No additional space used for sorting (in-place)
# - Total: O(n)
