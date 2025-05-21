# Encode and Decode Strings
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(n)
# Hint: Prefix each string with its length and a delimiter, then parse during decoding

def encode(strs):
    parts = []
    for s in strs:
        parts.append(str(len(s)) + "#" + s)
    return ''.join(parts)


def decode(s):
    result = []
    i = 0
    while i < len(s):
        n = ""
        while s[i] != "#":
            n += s[i]
            i += 1
        i += 1  
        length = int(n)
        word = s[i:i + length]
        result.append(word)
        i += length
    return result

# Time Complexity:
# - encode:
#     - Iterating through all strings: O(m), where m = number of strings
#     - Appending string with length prefix: O(len(s)) for each → total O(n)
#     - Final join: O(n)
# - decode:
#     - Scanning through the encoded string: O(n) where n = sum of lengths of all the strings
# Space Complexity:
# - encode:
#     - List `parts` stores encoded strings: O(m)
#     - Final encoded string: O(n)
# - decode:
#     - Result list stores all original strings: O(m)


strs = ["neet","code","love","you"]
encoded = encode(strs)
print(encoded)  # Output: "4#neet4#code4#love3#you"
decoded = decode(encoded)   
print(decoded)  # Output: ["neet","code","love","you"]
