import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # Time Complexity: O(nlogk)
        # Space Complexity: O(n)
        req = []
        n = len(heights)
        for i in range(n-1):
            if heights[i] < heights[i+1]:
                diff = heights[i+1]-heights[i]
                bricks -= diff
                heapq.heappush(req, -diff)
                if bricks < 0:
                    bricks += -heapq.heappop(req)
                    ladders -= 1
                if ladders < 0: return i                
        return n-1

# Approach:
# A priority queue is created to store the bricks used in each step in decreasing order. This queue is a max heap, meaning the largest element is at the top.
# At each step, the code calculates the height difference (diff) between the current building and the next building.
# If the height difference (diff) is less than or equal to 0, it means no additional bricks are required to climb to the next building, so the loop continues to the next iteration.
# If the height difference (diff) is greater than 0, it means additional bricks are required to climb to the next building. These bricks are deducted from the available bricks and added to the priority queue.
# If the remaining number of bricks becomes negative after deducting the required bricks, it means the available bricks are not sufficient to climb to the next building. In this case, the code uses a ladder from the priority queue by adding the largest previously deducted number of bricks to the available bricks and reducing the number of available ladders by 1.
# If the remaining number of ladders becomes negative, it means there are no ladders left, and the loop breaks.

# Time Complexity: O(nlogk)
# Space Complexity: O(n)
