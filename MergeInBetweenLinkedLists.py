# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Time complexity: O(n+m)
        # Space Complexity: O(1)
        start = ListNode()
        end = list1

        for index in range (b):
            if index == a - 1:
                start = end
            end = end.next

        start.next = list2

        while (list2.next is not None):
            list2 = list2.next

        list2.next = end.next
        end.next = None
        
        return list1

# Approach:
# Initialize two ListNodes, start to null and end to list1.
# Find the nodes at index a - 1 and b of list1. Traverse through list1 using a for loop with the iterator index from 0 to b - 1:
# If index equals a - 1 set start to end.
# Progress to the next node in list1 by setting end to end.next.
# Set start.next to list2.
# Find the tail of list2 by traversing the list with list2 = list2.next until the last node is reached.
# Set list2.next to end.next and set end.next to null. Note that the order of the statements is important.
# Return list1, which points to the head of the resultant linked list.
    
# Time complexity: O(n+m)
# Space Complexity: O(1)
