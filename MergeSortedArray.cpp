class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // Time Complexity: O(m+n)
        // Space Complexity: O(1)
        int p1 = m-1;
        int p2 = n-1;
        int k = m+n-1;
        while(p1 >= 0 && p2 >= 0) {
            if(nums1[p1] > nums2[p2]) {
                nums1[k] = nums1[p1];
                p1--;
            } else {
                nums1[k] = nums2[p2];
                p2--;
            }
            k--;
        }
        while(p2>=0) {
            nums1[k] = nums2[p2];
            p2--;
            k--;
        }
    }
};

// Approach:
// We can use the extra space in nums1 to store the larger elements.
// Take two pointers p1 and p2, starting from the end of the arrays nums1 and nums2 respectively.
// Take another pointer k starting at index m+n-1
// Compare the elements at p1 and p2, and place the larger element at index k, and update the pointers.
// Stop when all elements of nums2 are moved, i.e p2 < 0

// Time Complexity: O(m+n)
// Space Complexity: O(1)
