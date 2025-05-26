# Longest Substring Without Repeating Characters
# Overall Time Complexity: O(n) where n is the length of the string
# Overall Space Complexity: O(m) where m is the number of unique characters in the string.
# Hint: Sliding window (left and right pointers) + set to track unique characters

def lengthOfLongestSubstring(s):
    unique = set()
    l = 0
    max_length = 0
    for r in range(len(s)):
        while s[r] in unique:
            unique.remove(s[l])
            l += 1
        unique.add(s[r])
        max_length = max(max_length, r - l + 1)
    return max_length

# Time Complexity:
# - Outer loop traverses each character once: O(n)
# - Inner loop (while) moves the left pointer `l` to ensure no duplicates
# - Each character is added and removed from the set at most once
# Space Complexity:
# - The set `unique` stores at most `m` characters
# - In worst case (all unique characters in the string), space is O(m))

s = "zxyzxyz"
print(lengthOfLongestSubstring(s))  # Output: 3 
s = "xxxx"
print(lengthOfLongestSubstring(s))  # Output: 1
