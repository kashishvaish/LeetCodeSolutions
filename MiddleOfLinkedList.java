/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        // Time Complexity: O(n)
        // Space Complexity: O(1)
        ListNode slow = head;
        ListNode fast = head;
        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}

// Approach:
// Initialize two pointers, slow and fast, both pointing to the head of the list initially.
// Then, traverse the list using the fast pointer, which moves two steps at a time, and the slow pointer, which moves one step at a time.
// By the time the fast pointer reaches the end of the list, the slow pointer will be at the middle node.

// Time Complexity: O(n)
// Space Complexity: O(1)
