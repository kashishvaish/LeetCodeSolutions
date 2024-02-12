# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

# Approach:
# 1 -> 2 -> 3

# For 1:
# prev = None
# 1 -> None
# next = 2

# For 2:
# prev = 1
# 2 -> 1 -> None
# next = 3

# For 3:
# prev = 2
# 3 -> 2 -> 1 -> None
# next = None

# Time Complexity: O(n)
# Space Complexity: O(1)
