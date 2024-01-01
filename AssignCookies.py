class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Time Complexity: O(nlogn + mlogm)
        # Space Complexity: O(n + m) 
        g.sort(reverse = True)
        s.sort(reverse = True)
        c = 0
        j = 0
        n = len(s)
        for greed in g:
            if j >= n: break
            if greed > s[j]:
                continue
            else:
                c += 1
                j += 1
        return c

# Intuition - Greedy, Two-Pointer:
# Sort both greed and sizes arrays in descending order.
# Start allocating the largest available cookie to the children starting from the child with highest greed to lowest greed.
# Stop if no more cookies are left to assign.

# Time Complexity: O(nlogn + mlogm) due to sorting
# Space Complexity: O(n + m) due to sorting
