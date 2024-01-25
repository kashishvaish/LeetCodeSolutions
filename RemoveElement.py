class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(nums)
        i = 0
        k = n-1
        while i <= k:
            if nums[k] == val:
                k -= 1
            elif nums[i] == val:
                nums[i] = nums[k]
                i += 1
                k -= 1
            else:
                i += 1
        return i

# Two pointer Approach
# Initialize two pointers, i and k, where i starts from the beginning of the array, and k starts from the end of the array.
# Use a while loop to iterate through the array until i is less than or equal to k.
# Inside the loop:
# If nums[k] is equal to the target value val, decrement the k pointer to skip the occurrences of val at the end of the array.
# If nums[i] is equal to the target value val, replace nums[i] with the value at the k-th position. Then, increment i to move forward in the array, and decrement k to move backward.
# If neither of the above conditions is met, it means that the element at nums[i] is not equal to val. Increment i to move forward in the array.
# Continue this process until i is greater than k.
# The final value of i represents the length of the modified array, where all occurrences of val have been removed. Return this length.

# Time Complexity: O(n)
# Space Complexity: O(1)
