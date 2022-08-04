# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(m+n) where m and n are the length of linked lists
        # Space: O(m+n)
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode(0)
        curr = head
        carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            curr.next = ListNode(sum%10)
            curr = curr.next
            carry = sum // 10
            l1 = l1.next
            l2 = l2.next
        while l1:
            sum = l1.val + carry
            curr.next = ListNode(sum%10)
            curr = curr.next
            carry = sum // 10
            l1 = l1.next
        while l2:
            sum = l2.val + carry
            curr.next = ListNode(sum%10)
            curr = curr.next
            carry = sum // 10
            l2= l2.next
        if carry:
            curr.next = ListNode(carry)
        return head.next
        
# Approach

# Go through the two linked lists node by node --> calculating sum of corresponding digits and keeping track of carry.

# Time: O(m+n) where m and n are the length of linked lists
# Space: O(m+n)
