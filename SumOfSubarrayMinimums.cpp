class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        int n = arr.size();
        vector<int> left(n, -1);
        vector<int> right(n, n);
        stack<int> stk;
        for(int i = 0; i < n; i++) {
            while(!stk.empty() && arr[stk.top()] >= arr[i]) {
                stk.pop();
            }
            if(!stk.empty()) {
                left[i] = stk.top();
            }
            stk.push(i);
        }
        stk = stack<int>();
        for(int i = n-1; i >= 0; i--) {
            while(!stk.empty() && arr[stk.top()] > arr[i]) {
                stk.pop();
            }
            if(!stk.empty()) {
                right[i] = stk.top();
            }
            stk.push(i);
        }
        long long result = 0;
        int mod = 1e9 + 7;
        for(int i = 0; i < n; i++) {
            result += static_cast<long long>(i - left[i]) * (right[i] - i) * arr[i] % mod;
            result %= mod;
        }
        return result;
    }
};

// Naive Approach:
// For all subarrays, track the minimum element.
// Add all minimum elements.
// Return the sum modulo 10^9 + 7.

// Time Complexity: O(n^2)
// Space Complexity: O(1)


// Optimization:
// Create two arrays left and right such that,
// left[i] --> the index of first strictly smaller number on the left of arr[i]
// right[i] --> the index of first smaller or equal number on the right of arr[i] 
// Then, for each element the number of subarrays in which arr[i] will be minimum can be obtained using (i - left[i]) x (right[i] - i)
// Multiply the number of subarrays with arr[i], and add in the result.
// Return result mod 10^9 + 7.

// Example:
// arr = [3, 1, 2, 4]
// For 3, first smaller element towards left = None (-1)
//        first smaller element towards right = 1 (index 1)
// Number of subarrays in which 3 is minimum = 0-(-1) * (1-0) = 1
// [3]
// For 1, first smaller element towards left = None (-1)
//        first smaller element towards right = None (index n)
// Number of subarrays in which 1 is minimum = 1-(-1) * (4-1) = 2x3 = 6
// [1], [3, 1], [1, 2], [3, 1, 2], [3, 1, 2, 4], [1, 2, 4]
// For 2, first smaller element towards left = 1 (index 1)
//        first smaller element towards right = None (index n)
// Number of subarrays in which 2 is minimum = 2-(1) * (4-2) = 2
// [2], [2, 4]
// For 4, first smaller element towards left = 2 (index 2)
//        first smaller element towards right = None (index n)
// Number of subarrays in which 4 is minimum = 3-(2) * (4-3) = 1
// [4]

// Time Complexity: O(n)
// Space Complexity: O(n)
