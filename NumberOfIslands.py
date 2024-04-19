class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time Complexity: O(m x n)
        # Space Complexity: O(m x n)
        m = len(grid)
        n = len(grid[0])
        result = 0
        visited = [[False]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    result += 1
                    self.bfs(grid, visited, i, j, m, n)
        return result
    
    def bfs(self, grid, visited, i, j, m, n):
        q = [(i, j)]
        visited[i][j] = True
        while q:
            row, col = q.pop(0)
            dr = [-1, 0, 0, 1]
            dc = [0, -1, 1, 0]
            for i in range(4):
                r = row + dr[i]
                c = col + dc[i]
                if 0 <= r < m and 0 <= c < n and grid[r][c] == "1" and not visited[r][c]:
                    q.append((r, c))
                    visited[r][c] = True
                    
# Approach - BFS:
# Get the dimensions of the grid: m rows and n columns.
# Initialize result to store the count of islands.
# Initialize a 2D boolean array visited of size m x n to mark visited cells.
# Iterate through each cell in the grid using nested loops.
# For each cell (i, j):
# If the cell is land (grid[i][j] == "1") and has not been visited yet (not visited[i][j]):
# Increment the island count (result).
# Call the bfs function to perform BFS traversal from this cell, marking all connected land cells as visited.
# BFS Function:
# Initialize a queue q with the current cell (i, j).
# Mark the current cell as visited.
# While the queue is not empty:
# Dequeue a cell (row, col) from the queue.
# Explore the four adjacent cells (up, down, left, right).
# If a neighboring cell is within the grid boundaries, is land, and has not been visited:
# Enqueue the neighboring cell.
# Mark it as visited.
# After traversing all cells, the result variable contains the count of islands. Return this count.

# Time Complexity: O(m x n)
# Space Complexity: O(m x n)
