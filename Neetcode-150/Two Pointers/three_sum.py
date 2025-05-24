# Three Sum
# Overall Time Complexity: O(n^2)
# Overall Space Complexity: O(1) (excluding the output list)
# Hint: Sorting + Two-pointer technique

def threeSum(nums):
    output = []
    nums.sort()  
    for k in range(len(nums)):  
        if k > 0 and nums[k] == nums[k-1]:
            continue 
        if nums[k] > 0:
            break  
        target = -nums[k]
        i, j = k+1, len(nums)-1
        while i < j:  
            if nums[i]+nums[j] > target:
                j -= 1
            elif nums[i]+nums[j] < target:
                i += 1
            else:
                output.append([nums[i], nums[j], nums[k]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i-1]:  # Skip duplicates
                    i += 1
                while i < j and nums[j] == nums[j+1]:  # Skip duplicates
                    j -= 1
    return output

# Time Complexity:
# - Sorting the array: O(n log n)
# - Loop over all elements: O(n)
#   - Two-pointer scan per element: O(n)
# Space Complexity:
# - Uses only a few integer variables (i, j): O(1)
# - Output list not counted in space complexity

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
nums = [0, 1, 1]
print(threeSum(nums))  # Output: []
