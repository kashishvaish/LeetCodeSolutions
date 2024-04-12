class Solution:
    def trap(self, height: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(height)
        pre = [0]*n
        post = [0]*n
        result = 0
        pre[0] = height[0]
        for i in range(1, n):
            pre[i] = max(pre[i-1], height[i])
        post[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            post[i] = max(post[i+1], height[i])
        for i in range(n):
            result += min(pre[i], post[i]) - height[i]
        return result

# Approach:
# We start by initializing pre and post arrays of size n to store the maximum heights encountered from the left and right sides respectively. Additionally, we initialize result to accumulate the total trapped water.
# We traverse the height list from left to right, updating the pre array such that pre[i] holds the maximum height encountered from the left side up to index i. Similarly, we traverse from right to left, updating the post array such that post[i] holds the maximum height encountered from the right side up to index i.
# We traverse the height list again. At each index i, we calculate the amount of water that can be trapped above the current bar. This amount is the minimum of the maximum heights encountered from the left (pre[i]) and from the right (post[i]), minus the height of the current bar (height[i]). We add this amount to result.
# Finally, we return the accumulated result, which represents the total amount of trapped water between the bars.

# Time Complexity: O(n)
# Space Complexity: O(n)
