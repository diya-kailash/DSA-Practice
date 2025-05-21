# Group Anagrams
# Overall Time Complexity: O(m*n)
# Overall Space Complexity: O(m) 
# Hint: Hash array of each string as key in a hash map to group anagrams

from collections import defaultdict

def groupAnagrams(strs):
        hashmap = defaultdict(list)  
        for s in strs:  
            count = [0] * 26  
            for c in s:  
                count[ord(c) - ord('a')] += 1 
            hashmap[tuple(count)].append(s) 
        return list(hashmap.values()) 

# Time Complexity:
# - Initializing the hash map: O(1)
# - Iterating through m strings: O(m)
#   - For each string of length n:
#       - Creating count array: O(1)
#       - Populating count array: O(n)
#       - Converting to tuple and inserting into hashmap: O(1)
# - Returning hashmap values: O(m)
# Space Complexity:
# - Hash map stores up to m keys, each mapping to a list of strings: O(m)
# - Each key is a tuple of length 26 (fixed size): O(1)