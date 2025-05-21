# Valid Anagram
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(1)
# Hint: Fixed size hash array to count occurences of characters

def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0]*26 # O(1) space since it's a fixed array for lowercase letters
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += 1
            count[ord(t[i])-ord('a')] -= 1
        for val in count:
            if val != 0:
                return False
        return True

# Time Complexity:
# - Checking lengths: O(1)
# - Creating and initializing count array: O(1)
# - Iterating through both strings of length n: O(n)
#   - Character frequency updates: O(1) per operation
# - Final loop over 26 elements: O(1)

# Space Complexity:
# - Fixed-size array `count` of length 26 for lowercase letters: O(1)