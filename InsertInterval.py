class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(intervals)
        if n == 0: return [newInterval]
        res = []
        i = 0
        while i < n:
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
                i += 1
                if i >= n:
                        res.append(newInterval)
            else:
                if intervals[i][0] > newInterval[1]:
                    res.append(newInterval)
                    for j in range(i, n): res.append(intervals[j])
                    break
                else:
                    newInterval[0] = min(intervals[i][0], newInterval[0])
                    newInterval[1] = max(intervals[i][1], newInterval[1])
                    i += 1
                    if i >= n:
                        res.append(newInterval)
        return res
    
# Approach:
# Initialize an empty list res to store the merged intervals.
# Iterate through each interval in the intervals list. For each interval:
# If the end of the current interval is less than the start of the new interval (newInterval), it means there is no overlap, so add the current interval to res.
# If the start of the current interval is greater than the end of the new interval, it means there is no overlap, so add the new interval to res and append the remaining intervals from intervals to res.
# If there is an overlap between the current interval and the new interval, update the start and end of the new interval to encompass both intervals, and move to the next interval in intervals.
# If the loop ends and there are no more intervals in intervals, append the new interval to res.
# Return the merged intervals stored in res.

# Time Complexity: O(n)
# Space Complexity: O(1)
