# Longest Repeating Character Replacement
# Overall Time Complexity: O(n) where n is the length of the string
# Overall Space Complexity: O(m) where m is the number of unique characters in the string.
# Hint: Sliding window (left and right pointers) + hash map to track character frequencies

def characterReplacement(s, k):
    max_length = 0
    counts = {}
    l = 0
    max_freq = 0
    for r in range(len(s)):
        counts[s[r]] = 1 + counts.get(s[r], 0)
        max_freq = max(max_freq, counts[s[r]])
        while (r - l + 1) - max_freq > k:
            counts[s[l]] -= 1
            l += 1
        max_length = max(max_length, r - l + 1)
    return max_length

# Time Complexity:
# - Outer loop runs once for each character: O(n)
# - All dictionary operations (get, set, max) are O(1) 
# Space Complexity:
# - Dictionary `counts` stores character frequencies which is at most 'm'
# - In worst case (all unique characters in the string), space is O(m)

s = "AAABABB"
k = 1
print(characterReplacement(s, k))  # Output: 5

s = "XYYX"
k = 2
print(characterReplacement(s, k))  # Output: 4  
