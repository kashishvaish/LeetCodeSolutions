/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // Time: O(m+n) where m and n are the length of linked lists
        // Space: O(m+n)
        if(l1 == NULL)
            return l2;
        if(l2 == NULL)
            return l1;
        ListNode* head = new ListNode(0);
        ListNode* curr = head;
        int carry = 0;
        while(l1 || l2) {
            int num1 = l1 ? l1->val : 0;
            int num2 = l2 ? l2->val : 0;
            int sum = num1 + num2 + carry;
            curr->next = new ListNode(sum % 10);
            curr = curr->next;
            carry = sum / 10;
            if(l1)
                l1 = l1->next;
            if(l2)
                l2 = l2->next;
        }
        if(carry) {
            curr->next = new ListNode(carry);
        }
        return head->next;
    }
};
        
// Approach

// Go through the two linked lists node by node --> calculating sum of corresponding digits and keeping track of carry.
// Time: O(m+n) where m and n are the length of linked lists
// Space: O(m+n)
