class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Time Complexity: O(m x n)
        # Space Complexity: O(n)
        result = 0
        rows = len(matrix)
        cols = len(matrix[0])
        hist = [0]*cols
        for row in matrix:
            for i in range(cols):
                if row[i] == "1": hist[i] += 1
                else: hist[i] = 0
            result = max(result, self.getmaxarea(hist))
        return result
    
    def getmaxarea(self, hist):
        answer = 0
        n = len(hist)
        stack = []
        for i in range(n+1):
            while stack and (i == n or hist[i] < hist[stack[-1]]):
                h = hist[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                answer = max(answer, h * w)
            stack.append(i)
        return answer
    
# Approach:
# Initialize result to store the maximum rectangle area found.
# Determine the number of rows and columns in the matrix.
# Create a histogram hist of length equal to the number of columns, initialized with zeros.
# Iterate through each row of the matrix.
# For each row:
# Update the histogram hist:
# If the value in the matrix is '1', increment the corresponding bar's height in the histogram.
# If the value is '0', reset the height of the bar to 0.
# For each updated histogram hist, calculate the maximum area of the rectangle:
# Utilize a stack-based approach to efficiently find the maximum area.
# Iterate through the histogram bars:
# While the stack is not empty and the current bar's height is less than the height of the bar at the top of the stack:
# Pop the top index from the stack.
# Calculate the area with the popped bar's height and update the maximum area (answer) accordingly.
# Push the current index onto the stack.
# Return the maximum area found.
# Return Result: result will hold the value of the largest rectangle that can be formed within the binary matrix.
    
# Time Complexity: O(m x n)
# Space Complexity: O(n)
