class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Time: O(log(m+n))
        // Space: O(1)
        if(nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }
        int m = nums1.size();
        int n = nums2.size();
        int total = m+n;
        int medianPos = (total+1) / 2;
        int start = 0;
        int end = m;
        while(start <= end) {
            int mid = (start+end)/2;
            int j = medianPos - mid;
            
            int l1 = (mid==0) ? INT_MIN : nums1[mid-1];
            int l2 = (j==0) ? INT_MIN : nums2[j-1];
            int r1 = (mid==m) ? INT_MAX : nums1[mid];
            int r2 = (j==n) ? INT_MAX : nums2[j];
            
            if((l1 <= r2) && (l2 <= r1)) {
                if(total & 1) {
                    return max(l1, l2); 
                } else {
                    return (max(l1, l2) + min(r1, r2)) / 2.0;
                }
            } else if(l1 > r2) {
                end = mid-1;
            } else {
                start = mid+1;
            }
        }
        return 0.0;
    }
};

// Median:
//     1, 2, 3 --> odd length --> median at len//2 --> 1

//     1, 2, 3, 4 --> even length --> median is avg of nums at len//2 and len//2-1 --> 2.5

    
// 1. Naive Approach

// Merge both the arrays into a single sorted array --> return median value
// Time: O(m + n)
// Space: O(m + n)


// 2. Space Optimization

// Instead of merging both arrays and storing separately --> keep count of the number of values while traversing both the arrays and return the value at median position. 
// Time: O(m+n)
// Space: O(1)


// 3. Binary Search

// The idea here is to --> divide both arrays into left and right halves such that the values in the left halves of both the arrays will be the values lying left of the median value and values in right halves of both the arrays will be the values lying right of the median value.
// Time: O(log(m+n))
// Space: O(1)
