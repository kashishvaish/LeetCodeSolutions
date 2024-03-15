class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(nums)
        res = [1]*n
        preproduct = 1
        postproduct = 1
        for i in range(n):
            res[i] = preproduct
            preproduct *= nums[i]
        for i in range(n-1, -1, -1):
            res[i] *= postproduct
            postproduct *= nums[i]
        return res

# Approach:
# Initialize three lists, pre, post, and res, each of size n, to store the products.
# Initialize two variables, preproduct and postproduct, to 1. These will keep track of the running product before and after the current index, respectively.
# Iterate through the nums list to calculate the products before each index and store them in the pre list. Update preproduct by multiplying it with the current number at each iteration.
# Iterate through the nums list in reverse order to calculate the products after each index and store them in the post list. Update postproduct by multiplying it with the current number at each iteration.
# Simultaneously, calculate the final result by multiplying the corresponding elements from the pre and post lists and store them in the res list.
# Return the res list containing the product of all elements except itself for each element in the original nums list.
    
# Code:
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         # Time Complexity: O(n)
#         # Space Complexity: O(n)
#         n = len(nums)
#         pre = [0]*n
#         post = [0]*n
#         res = [0]*n
#         preproduct = 1
#         postproduct = 1
#         for i in range(n):
#             pre[i] = preproduct
#             preproduct *= nums[i]
#         for i in range(n-1, -1, -1):
#             post[i] = postproduct
#             res[i] = pre[i]*post[i]
#             postproduct *= nums[i]
#         return res
    
# Time Complexity: O(n)
# Space Complexity: O(n)



# Space Optimization:
# Initialize a list, res, of size n, where n is the length of the input list nums, to store the final result.
# Initialize two variables, preproduct and postproduct, to 1. These variables represent the running product before and after the current index, respectively.
# Iterate through the nums list to calculate the products before each index and store them directly in the res list. Update preproduct by multiplying it with the current number at each iteration.
# Iterate through the nums list in reverse order to calculate the products after each index and directly update the corresponding elements in the res list by multiplying them with postproduct. Update postproduct by multiplying it with the current number at each iteration.
# Finally, return the res list containing the product of all elements except itself for each element in the original nums list.

# Code:
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         # Time Complexity: O(n)
#         # Space Complexity: O(1)
#         n = len(nums)
#         res = [1]*n
#         preproduct = 1
#         postproduct = 1
#         for i in range(n):
#             res[i] = preproduct
#             preproduct *= nums[i]
#         for i in range(n-1, -1, -1):
#             res[i] *= postproduct
#             postproduct *= nums[i]
#         return res

# Time Complexity: O(n)
# Space Complexity: O(1)
