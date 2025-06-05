# Top K Frequent Elements 
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(n)
# Hint: Hash map to count frequencies and frequency bucket list to group elements

def topKFrequent(nums, k):
    hashmap = {}
    freq = [[] for _ in range(len(nums) + 1)]
    for n in nums:
        hashmap[n] = 1 + hashmap.get(n, 0)
    for n, c in hashmap.items():
        freq[c].append(n)
    result = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            result.append(n)
            if len(result) == k:
                return result

# Time Complexity:
# - Counting frequencies in hashmap: O(n)
# - Filling frequency buckets: O(n)
# - Iterating from high to low frequency to collect top k: O(n)
# Space Complexity:
# - Hash map stores frequency of up to n unique elements: O(n)
# - Frequency list with n+1 buckets: O(n)
# - Result list storing k elements: O(k), which is O(n) in worst-case

nums = [1,2,2,3,3,3]
k = 2
result = topKFrequent(nums, k)
print(result)  # Output: [3, 2]