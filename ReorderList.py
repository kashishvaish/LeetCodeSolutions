# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        if not head or not head.next: return head
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        first = head
        second = self.reverse(slow)
        head = ListNode()
        curr = head
        while first and second:
            curr.next = first
            first = first.next
            curr.next.next = second
            second = second.next
            curr = curr.next.next
        if second != None: curr.next = second
        return head.next
        
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

# Approach:
# Check if the linked list is empty or has only one node. If so, return the head as there's no need to reorder a single node or an empty list.
# Initialize slow and fast pointers to find the middle of the list. Also, initialize a prev variable to keep track of the node before the slow pointer.
# Traverse the list using slow and fast pointers to find the middle node. For each step, move the slow pointer one step and the fast pointer two steps.
# After finding the middle node, split the list into two halves by updating the next pointer of the node before the middle node to None.
# Reverse the second half of the list using the reverse function.
# Merge the first and reversed second halves alternately to reorder the list.
# Return the modified head.

# Time Complexity: O(n)
# Space Complexity: O(1)
