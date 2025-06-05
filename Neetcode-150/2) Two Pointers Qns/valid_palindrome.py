# Valid Palindrome
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(1)
# Hint: Two-pointer technique - i at beginning and j at end, move inward

def isPalindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while j > i and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():  
            return False
        i += 1
        j -= 1
    return True

# Time Complexity:
# - Scans each character at most once: O(n)
#   - Comparing valid characters: O(1)
# Space Complexity:
# - Uses only a few integer variables (i, j): O(1)

s = "Was it a car or a cat I saw?"
print(isPalindrome(s))  # Output: True
s = "tab a cat"
print(isPalindrome(s)) # Output: False