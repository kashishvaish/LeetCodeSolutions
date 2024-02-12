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
    public ListNode reverseList(ListNode head) {
        // Time Complexity: O(n)
        // Space Complexity: O(1)
        ListNode prev = null;
        ListNode next = null;
        while(head != null) {
            next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }
        return prev;
    }
}

// Approach:
// 1 -> 2 -> 3

// For 1:
// prev = None
// 1 -> None
// next = 2

// For 2:
// prev = 1
// 2 -> 1 -> None
// next = 3

// For 3:
// prev = 2
// 3 -> 2 -> 1 -> None
// next = None

// Time Complexity: O(n)
// Space Complexity: O(1)
