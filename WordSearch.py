class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Time Complexity: O(m * n * 4^l)
        # Space Complexity: O(l)
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if self.check(i, j, board, word, m, n): return True
        return False
    
    def check(self, row, col, board, word, m, n):
        if word == "": return True
        if board[row][col] != word[0]:
            return False
        if len(word) == 1: return True
        temp = board[row][col]
        board[row][col] = -1
        dr = [-1, 0, 0, 1]
        dc = [0, -1, 1, 0]
        ans = False
        for i in range(4):
            r = row + dr[i]
            c = col + dc[i]
            if 0 <= r < m and 0 <= c < n:
                ans = ans or self.check(r, c, board, word[1:], m, n)
        board[row][col] = temp
        return ans
    
# Approach:
# The exist function iterates over each cell in the board using two nested loops. For each cell (i, j):
# It calls the check function to determine if the word can be formed starting from that cell. If check returns True, it means the word can be formed, so the exist function returns True.
# If no cell is found that can form the word, the exist function returns False after checking all cells.

# The check function is a recursive function that explores the neighboring cells of the current cell (row, col) to find the characters of the word.
# It first checks if the current cell's character matches the first character of the word. If not, it returns False.
# If the length of the word is 1, it means that the current cell's character matches the last character of the word, so it returns True.
# It temporarily stores the current cell's character, marks the cell as visited (by changing its value to -1), and explores the neighboring cells recursively.
# After exploring all neighboring cells, it restores the original value of the current cell and returns the result.

# Time Complexity: O(m * n * 4^l), where m and n are the dimensions of the board and l is the length of the word.
# Space Complexity: O(l), where l is the length of the word, due to the recursive calls on the call stack.
