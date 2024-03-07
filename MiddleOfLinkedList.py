# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
# Approach:
# Initialize two pointers, slow and fast, both pointing to the head of the list initially.
# Then, traverse the list using the fast pointer, which moves two steps at a time, and the slow pointer, which moves one step at a time.
# By the time the fast pointer reaches the end of the list, the slow pointer will be at the middle node.

# Time Complexity: O(n)
# Space Complexity: O(1)
