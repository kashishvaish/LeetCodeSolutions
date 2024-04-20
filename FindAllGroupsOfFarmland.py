class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # Time Complexity: O(m x n)
        # Space Complexity: O(1)
        m = len(land)
        n = len(land[0])
        result = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    self.util(land, result, i, j, m, n)
        return result
                    
    def util(self, land, result, row, col, m, n):
        r = row
        c = col
        while r+1 < m and land[r+1][c] == 1:
            r += 1
        while c+1 < n and land[r][c+1] == 1:
            c += 1
        for i in range(row, r+1):
            for j in range(col, c+1):
                land[i][j] = 0
        result.append([row, col, r, c])
        
# Approach:
# Get the dimensions of the grid: m rows and n columns.
# Initialize an empty list result to store the coordinates of farmland rectangles.
# Iterate through each cell in the grid using nested loops.
# For each cell (i, j):
# If the cell represents farmland (land[i][j] == 1), call the util function to find the boundaries of the farmland and update the grid accordingly.

# Utility Function (util):
# Starting from the current cell (row, col), find the bottom-right corner of the farmland by traversing horizontally and vertically until reaching the boundary of the farmland.
# Update the grid to mark the cells of the farmland as visited (set them to 0).
# Append the coordinates of the farmland rectangle ([row, col, r, c], where (row, col) is the top-left corner and (r, c) is the bottom-right corner) to the result list.

# After traversing all cells, the result list contains the coordinates of all farmland rectangles. Return this list.

# Time Complexity: O(m x n)
# Space Complexity: O(1)
