class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // Time Complexity: O(n)
        // Space Complexity: O(1)
        int potential = nums[0];
        int freq = 0;
        for(int num: nums) {
            if(num == potential) freq++;
            else {
                if(freq == 1) potential = num;
                else freq--;
            }
        }
        return potential;
    }
};

// Naive Approach:
// Count frequency of all elements. --> Return element with frequency greater than n/2

// Time Complexity: O(n)
// Space Complexity: O(n)


// Optimization: Moore’s Voting Algorithm
// This algorithm works on the fact that if an element occurs more than N/2 times, it means that the remaining elements other than this would definitely be less than N/2.
// We will keep track of the candidate element and its count.
// When the elements are the same as the candidate element, votes are incremented whereas when some other element is found (not equal to the candidate element), we decreased the count.
// This actually means that we are decreasing the priority of winning ability of the selected candidate.
// When votes become 0, this actually means that there are the equal  number of votes for different elements, which should not be the case for the element to be the majority element. So the candidate element cannot be the majority and hence we choose the present element as the candidate and continue the same till all the elements get finished.
// The final candidate would be our majority element.

// Time Complexity: O(n)
// Space Complexity: O(1)
