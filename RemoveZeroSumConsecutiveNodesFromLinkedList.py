# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        front = ListNode(0, head)
        curr = front
        prefixsum = 0
        d = {0:front}
        while curr:
            prefixsum += curr.val
            d[prefixsum] = curr
            curr = curr.next
        prefixsum = 0
        curr = front
        while curr:
            prefixsum += curr.val
            curr.next = d[prefixsum].next
            curr = curr.next
        return front.next
    
# Approach:
# Initialize a new ListNode front with the value 0 whose next field points to head and a node current to front.
# Initialize a variable prefixsum to 0 and a hashmap d, which stores integer, ListNode pairs. The key is the prefix sum, and the value is the corresponding ListNode. Add front to the hashmap.
# Process all of the nodes in the linked list, while current != null:
    # Add current's value to prefixsum.
    # Add the prefix sum and node pair to the hashmap.
    # Set current to current.next.
# Reset prefixSum to 0 and current to front.
# Process all of the nodes in the linked list, while current != null:
    # Add current's value to prefixSum.
    # Make a connection from current to the last node after the zero-sum consecutive sequence by setting current.next to prefixSumToNode[prefixSum].next.
    # Set current to current.next.
# Return front.next. The front points to the head of the final linked list.

# Time Complexity: O(n)
# Space Complexity: O(n)
