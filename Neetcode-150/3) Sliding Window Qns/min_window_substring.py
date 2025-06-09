# Minimum Window Substring
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(k)
# Hint: Sliding window with two hashmaps to track character counts and match progress

def minWindow(s, t):
    if len(t) > len(s) or not t:
        return ""
    counts = {}
    window = {}
    for c in t:
        counts[c] = 1 + counts.get(c, 0)
    have, need = 0, len(counts)
    result = [-1, -1]
    length = float('inf')
    l = 0
    for r in range(len(s)):
        ch = s[r]
        window[ch] = 1 + window.get(ch, 0)
        if ch in counts and window[ch] == counts[ch]:
            have += 1
        while have == need:
            if (r - l + 1) < length:
                result = [l, r]
                length = (r - l + 1)
            window[s[l]] -= 1
            if s[l] in counts and window[s[l]] < counts[s[l]]:
                have -= 1
            l += 1
    l, r = result
    return s[l:r + 1] if length != float('inf') else ""

# Time Complexity:
# - Building target count map: O(m), where m = len(t)
# - Sliding window over s: O(n), where n = len(s)
# - Each character is added and removed from window at most once
# - Total: O(n) since m ≤ n

# Space Complexity:
# - counts and window hashmaps store up to k unique characters 
# - Other variables use O(1) space
# - Total: O(k), where k = number of unique characters in s and t

s = "xyz"
t = "xyz"
print(minWindow(s, t))  # "xyz"
s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))  # "BANC"
s = "x"
t = "xy"
print(minWindow(s, t))  # ""


