# Car Fleet
# Overall Time Complexity: O(n log n)
# Overall Space Complexity: O(n)
# Hint: Sort by position, store time to reach target in a stack

def carFleet(target, position, speed):
    stack = []
    pairs = [(p, s) for p, s in zip(position, speed)]
    pairs.sort(reverse=True)  # Sort cars by starting position, farthest to closest
    for p, s in pairs:
        hours = (target - p) / s
        stack.append(hours)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()  # Merge with the previous fleet
    return len(stack)

# Time Complexity:
# - Creating pairs: O(n)
# - Sorting pairs by position: O(n log n)
# - Iterating over sorted pairs: O(n)
# - Total: O(n log n)
# Space Complexity:
# - Stack to track fleets: O(n)
# - List of pairs (position, speed): O(n)
# - Total: O(n)

target = 10
position = [1,4]
speed = [3,2]
print(carFleet(target, position, speed))  # Output: 1
target = 10
position = [4,1,0,7]
speed = [2,2,1,1]
print(carFleet(target, position, speed))  # Output: 3


