class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Time: O(log(m+n))
        # Space: O(1)
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        m = len(nums1)
        n = len(nums2)
        total = m + n
        start = 0
        end = m
        midPos = (total+1) // 2
        while start <= end:
            mid = (start+end)//2
            j = midPos - mid
            l1 = float('-inf') if mid==0  else nums1[mid-1]
            l2 = float('-inf') if j==0 else nums2[j-1]
            r1 = float('inf') if mid==m  else nums1[mid]
            r2 = float('inf') if j==n else nums2[j]
            
            if l1 <= r2 and l2 <= r1:
                if total & 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                end = mid-1
            else:
                start = mid+1
        return 0

# Median:
    # 1, 2, 3 --> odd length --> median at len//2 --> 1

    # 1, 2, 3, 4 --> even length --> median is avg of nums at len//2 and len//2-1 --> 2.5

    
# 1. Naive Approach

# Merge both the arrays into a single sorted array --> return median value
# Time: O(m + n)
# Space: O(m + n)


# 2. Space Optimization

# Instead of merging both arrays and storing separately --> keep count of the number of values while traversing both the arrays and return the value at median position. 
# Time: O(m+n)
# Space: O(1)


# 3. Binary Search

# The idea here is to --> divide both arrays into left and right halves such that the values in the left halves of both the arrays will be the values lying left of the median value and values in right halves of both the arrays will be the values lying right of the median value.
# Time: O(log(m+n))
# Space: O(1)
