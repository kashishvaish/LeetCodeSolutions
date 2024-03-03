# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        total = 0
        temp = head
        while temp:
            total += 1
            temp = temp.next
            
        index = total - n
        if index == 0: return head.next
        prev = None
        curr = head
        c = 0
        while c < index:
            prev = curr
            curr = curr.next
            c += 1
        prev.next = curr.next
        return head

    
# Approach:
# First traverse the entire list to count the total number of nodes.
# With this count, calculate the index of the node to be removed from the beginning of the list.
# Then, traverse the list again, stopping at the node just before the target node to adjust the pointers and remove the target node.
# Handle the special case where the target node is the head of the list.  

# Example:
# head = [1,2,3,4,5], n = 2
# total = 5
# index = 5 - 2 = 3
# Initialize c to 0, iterate till c < 3

# c = 0
# prev = 1
# curr = 2

# c = 1
# prev = 2
# curr = 3

# c = 2
# prev = 3
# curr = 4

# Make 3.next equal to 4.next --> this will effectively remove 4 from the linked list.
# Finally, return the head


# Time Complexity: O(n)
# Space Complexity: O(1)
