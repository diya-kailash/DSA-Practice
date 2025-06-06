# Permutation in String
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(1)
# Hint: Use fixed-size sliding window with frequency comparison

def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    s1_count, s2_count = [0]*26, [0]*26
    for i in range(len(s1)):
        s1_count[ord(s1[i])-ord('a')] += 1
        s2_count[ord(s2[i])-ord('a')] += 1
    matches = 0
    for i in range(26):
        if s1_count[i] == s2_count[i]:
            matches += 1
    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True

        index = ord(s2[r]) - ord('a')
        s2_count[index] += 1
        if s2_count[index] == s1_count[index]:
            matches += 1
        elif s1_count[index] + 1 == s2_count[index]:
            matches -= 1

        index = ord(s2[l]) - ord('a')
        s2_count[index] -= 1
        if s2_count[index] == s1_count[index]:
            matches += 1
        elif s1_count[index] - 1 == s2_count[index]:
            matches -= 1

        l += 1
    return matches == 26

# Time Complexity:
# - Initial frequency setup: O(26) = O(1)
# - First window frequency fill: O(len(s1))
# - Sliding window over s2: O(len(s2))
# - Total: O(n), where n = len(s2)
# Space Complexity:
# - Frequency arrays of size 26 (for a-z): O(1)
# - No extra space depending on input size

s1 = "abc"
s2 = "lecabee"
print(checkInclusion(s1, s2)) # True
s1 = "abc"
s2 = "lecaabee"
print(checkInclusion(s1, s2)) # False
