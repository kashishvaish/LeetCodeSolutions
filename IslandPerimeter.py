class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(m x n)
        # Space Complexity: O(1)
        res = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0: res += 1
                    if j == 0 or grid[i][j-1] == 0: res += 1
                    if i == m-1 or grid[i+1][j] == 0: res += 1
                    if j == n-1 or grid[i][j+1] == 0: res += 1
        return res
    
# Approach:
# Initialize res to store the perimeter count.
# Get the dimensions of the grid: m rows and n columns.
# Use nested loops to iterate over each cell in the grid.
# For each land cell (grid[i][j] == 1):
# Check if the cell is on the boundary of the grid or adjacent to water cells. If so, increment the perimeter count accordingly:
# If the current cell is on the top row (i == 0) or the cell above it is water (grid[i-1][j] == 0), increment the perimeter.
# If the current cell is on the leftmost column (j == 0) or the cell to its left is water (grid[i][j-1] == 0), increment the perimeter.
# If the current cell is on the bottom row (i == m-1) or the cell below it is water (grid[i+1][j] == 0), increment the perimeter.
# If the current cell is on the rightmost column (j == n-1) or the cell to its right is water (grid[i][j+1] == 0), increment the perimeter.
# After traversing the entire grid, the res variable contains the total perimeter of the island. Return this value.
    
# Time Complexity: O(m x n)
# Space Complexity: O(1)
