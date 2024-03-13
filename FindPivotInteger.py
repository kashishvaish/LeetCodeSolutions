class Solution:
    def pivotInteger(self, n: int) -> int:
        # Time Complexity: O(logn)
        # Space Complexity: O(1)
        start = 1
        end = n
        total = n*(n+1)/2
        while start <= end:
            i = (start+end)//2
            pre = i*(i+1)/2
            post = total - pre + i
            if pre == post: return i
            elif pre < post: start = i+1
            else: end = i-1
        return -1

# Approach - Using Math formula:
# Begin by iterating through the integers from 1 to n using a for loop.
# For each integer i in the range, calculate the sum of integers from 1 to i (inclusive) and store it in the variable pre.
# Calculate the sum of integers from 1 to n (inclusive) and subtract pre from it. Then, add i to the result, and store it in the variable post.
# Check if pre is equal to post. If they are equal, it means that the integer i is the pivot integer. Return i.
# If no pivot integer is found after iterating through all integers from 1 to n, return -1.
    
# Code:
# class Solution:
#     def pivotInteger(self, n: int) -> int:
#         # Time Complexity: O(n)
#         # Space Complexity: O(1)
#         for i in range(1, n+1):
#             pre = i*(i+1)/2
#             post = n*(n+1)/2 - pre + i
#             if pre == post: return i
#         return -1
    
# Time Complexity: O(n)
# Space Complexity: O(1)



# Binary Search:
# Initialize two variables, start and end, representing the range of integers to search within. Set start to 1 and end to n.
# Calculate the total sum of integers from 1 to n (inclusive) and store it in the variable total.
# Enter a while loop that continues until the start pointer is less than or equal to the end pointer.
# Inside the loop, calculate the midpoint, i, as the floor division of the sum of start and end by 2.
# Calculate the pre-sum and post-sum using the formulas provided: pre = i*(i+1)/2 and post = total - pre + i.
# Check if pre is equal to post. If it is, return i as the pivot integer.
# If pre is less than post, update the start pointer to i+1, indicating that the pivot integer lies to the right of i.
# If pre is greater than post, update the end pointer to i-1, indicating that the pivot integer lies to the left of i.
# If no pivot integer is found after exiting the loop, return -1.

# Code:
# class Solution:
#     def pivotInteger(self, n: int) -> int:
#         # Time Complexity: O(logn)
#         # Space Complexity: O(1)
#         start = 1
#         end = n
#         total = n*(n+1)/2
#         while start <= end:
#             i = (start+end)//2
#             pre = i*(i+1)/2
#             post = total - pre + i
#             if pre == post: return i
#             elif pre < post: start = i+1
#             else: end = i-1
#         return -1

# Time Complexity: O(logn)
# Space Complexity: O(1)
