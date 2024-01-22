class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(nums)
        repeat = 0
        miss = 0
        for i in range(n):
            ind = abs(nums[i])-1
            if nums[ind] < 0: repeat = abs(nums[i])
            else: nums[ind] *= -1
        for i in range(n):
            if nums[i] > 0:
                miss = i+1
                break
        return [repeat, miss]

# Approach: 
# Store the frequencies of each element.
# Return the elements with 0 and 2 frequencies.

# Code:
# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#         # Time Complexity: O(n)
#         # Space Complexity: O(n)
#         n = len(nums)
#         freq = [0]*(n+1)
#         for num in nums:
#             freq[num] += 1
#         result = [0, 0]
#         for i in range(1, n+1):
#             if result[0] != 0 and result[1] != 0: break
#             elif freq[i] == 0: result[1] = i
#             elif freq[i] == 2: result[0] = i
#         return result

# Time Complexity: O(n)
# Space Complexity: O(n)



# Space Optimization:
# We will traverse through the numbers and since the numbers are in the range 1 to n, we will make the number with index equal to element - 1 negative. This will indicate the occurence of the element. If a number is already negative, it will indicate duplicacy. To identify the missing number, we'll iterate again to find the index with positive number.

# Code:
# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#         # Time Complexity: O(n)
#         # Space Complexity: O(1)
#         n = len(nums)
#         repeat = 0
#         miss = 0
#         for i in range(n):
#             ind = abs(nums[i])-1
#             if nums[ind] < 0: repeat = abs(nums[i])
#             else: nums[ind] *= -1
#         for i in range(n):
#             if nums[i] > 0:
#                 miss = i+1
#                 break
#         return [repeat, miss]

# Time Complexity: O(n)
# Space Complexity: O(1)
