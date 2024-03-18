class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)
        n = len(points)
        points.sort(key=lambda x: x[1])
        curr = points[0][1]
        arrow = 1
        for i in range(1, n):
            if points[i][0] > curr:
                arrow += 1
                curr = points[i][1]
        return arrow

# Approach:
# Sort the points array based on the end coordinates of each balloon interval. This ensures that the balloons with the smallest end coordinates come first.
# Initialize a variable curr to store the end coordinate of the first balloon in the sorted array. Also, initialize a variable arrow to count the number of arrows needed, starting with one arrow.
# Iterate through the sorted array of points starting from the second balloon. For each balloon:
# If the start coordinate of the current balloon is greater than the curr, it means the current balloon is not overlapping with the previous balloon. In this case, increment the arrow count by 1, and update curr to the end coordinate of the current balloon.
# After iterating through all balloons, return the final value of arrow, which represents the minimum number of arrows needed to burst all balloons.

# Time Complexity: O(nlogn) due to sorting
# Space Complexity: O(n) due to sorting
