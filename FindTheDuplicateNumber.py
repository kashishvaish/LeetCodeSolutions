class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

# Approach: Slow and fast pointer
# The key intuition behind this method is that if there's a cycle in the linked list, the fast and slow pointers will eventually meet.
# We treat the array as a linked list, where the index represents the node and the value at that index represents the next node.
# Using the fast-slow pointers technique, we traverse the linked list.
# The slow pointer moves one step at a time while the fast pointer moves two steps at a time.
# If there's a cycle in the linked list (indicating a duplicate number), the fast and slow pointers will eventually meet.
# After identifying the meeting point, we reset the slow pointer to the start and move both pointers at the same pace until they meet again. The meeting point will be the duplicate number.
    
# Time Complexity: O(n)
# Space Complexity: O(1)
