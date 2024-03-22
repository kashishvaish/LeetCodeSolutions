# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        
        # If the list is empty, it's a palindrome
        if not head or not head.next: return True
        
        # Initialize slow and fast pointers to find the middle of the list
        slow = head
        fast = head
        
        # Move slow pointer one step and fast pointer two steps at a time
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the list
        rev = self.reverse(slow)
        
        # Compare values of corresponding nodes in both halves
        while rev:
            if head.val != rev.val: return False
            head = head.next
            rev = rev.next
        
        # If all values match, the list is a palindrome
        return True

    def reverse(self, head):
        curr = head
        prev = None
        
        # Reverse the linked list
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # Return the head of the reversed list
        return prev
    
# Approach:
# Check if the linked list is empty or has only one node. If so, it's considered a palindrome, so return True.
# Initialize slow and fast pointers to find the middle of the list.
# Traverse the list using slow and fast pointers to find the middle node. For each step, move the slow pointer one step and the fast pointer two steps.
# After finding the middle node, reverse the second half of the list using the reverse function.
# Traverse both halves of the list simultaneously, and compare the values of corresponding nodes. If any values don't match, return False, indicating that the list is not a palindrome.
# If all values match, return True, indicating that the list is a palindrome.

# Time Complexity: O(n)
# Space Complexity: O(1)
