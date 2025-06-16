# Detect Squares (Count Axis-Aligned Squares in a 2D Plane)
# Overall Time Complexity:
#   - add(): O(1)
#   - count(): O(n), where n is the number of added points
# Overall Space Complexity: O(n)
# Hint: Check if square is formed with the query point based on distance and coordinates from other points

from collections import defaultdict
class CountSquares:
    def __init__(self):
        self.points = defaultdict(int)  # Maps each (x, y) → frequency
        self.pts = []                   # Stores all added points (including duplicates)

    def add(self, point):
        self.points[tuple(point)] += 1  
        self.pts.append(point)          

    def count(self, point):
        count = 0
        px, py = point
        for x, y in self.pts:  
            # Check if (px, py) and (x, y) can be diagonally opposite in a square
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            p1 = (px, y)
            p2 = (x, py)
            count += self.points[p1] * self.points[p2]  
        return count

# Time Complexity:
# - add():
#   - Insertion into dictionary and list: O(1)
# - count():
#   - Iterates over all added points: O(n)
#   - Dictionary lookups for potential square corners: O(1) each
# Space Complexity:
# - Dictionary stores frequency of each unique point: O(u), where u ≤ n
# - List stores every point added (including duplicates): O(n)
