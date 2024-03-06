# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False
    
# Floyd’s Cycle-Finding Algorithm:
# Suppose there are two people running on a track one with a speed x and another with a speed 2x (twice of first) now it's clear that person 2 is faster.
# Now assume the track to be circular and now since peson 2 will have faster speed so it is very sure that person two will meet person 1 or he will overtake him.

# Approach:
# Traverse linked list using two pointers.
# Move one pointer(slow) by one and another pointer(fast) by two.
# If these pointers meet at the same node then there is a loop. If pointers do not meet then the linked list doesn’t have a loop.

# Time Complexity: O(n)
# Space Complexity: O(1)
