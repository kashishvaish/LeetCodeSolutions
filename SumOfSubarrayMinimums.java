class Solution {
    public int sumSubarrayMins(int[] arr) {
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        int n = arr.length;
        int[] left = new int[n];
        int[] right = new int[n];
        Arrays.fill(left, -1);
        Arrays.fill(right, n);
        Stack <Integer> stack = new Stack<>();
        for(int i = 0; i < n; i++) {
            while(!stack.isEmpty() && arr[stack.peek()] >= arr[i]) {
                stack.pop();
            }
            if(!stack.isEmpty()) {
                left[i] = stack.peek();
            }
            stack.push(i);
        }
        stack.clear();
        for(int i = n-1; i >= 0; i--) {
            while(!stack.isEmpty() && arr[stack.peek()] > arr[i]) {
                stack.pop();
            }
            if(!stack.isEmpty()) {
                right[i] = stack.peek();
            }
            stack.push(i);
        }
        long result = 0;
        int mod = (int) 1e9 + 7;
        for(int i = 0; i < n; i++) {
            result += (long) (i - left[i]) * (right[i] - i) % mod * arr[i] % mod;
            result %= mod;
        }
        return (int) result;
    }
}

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
