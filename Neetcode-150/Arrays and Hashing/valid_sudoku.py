# Valid Sudoku
# Overall Time Complexity: O(n^2)
# Overall Space Complexity: O(n^2)
# Hint: Hash set corresponding to each row, column, and 3x3 square to track duplicates in them

from collections import defaultdict
def isValidSudoku(board):
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c]  in rows[r] or 
                board[r][c] in cols[c] or 
                board[r][c] in squares[(r//3, c//3)]):
                return False
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r//3, c//3)].add(board[r][c])
    return True

# Time Complexity:
# - Outer loop over 9 rows: O(9)
# - Inner loop over 9 columns per row: O(9)
#   - For each cell:
#       - Set lookup: O(1) average-case
#       - Set insert: O(1) average-case
# - Total: O(1) since the board size is fixed otherwise O(n^2) where n is the number of cells in a row
# Space Complexity:
# - Three defaultdicts with 9 sets each in row, column, and squares containing up to 9 elements
# - Total: O(9^2) which is O(1) for fixed size board
# For a generalized n x n board:
# - rows: n sets, each with up to n elements → O(n^2)
# - cols: n sets, each with up to n elements → O(n^2)
# - boxes: (n/√n)^2 = n boxes, each with up to n elements → O(n^2)
# - Total: O(n^2)

board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board)) # Output: False