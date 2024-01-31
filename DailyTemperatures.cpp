class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        int n = temperatures.size();
        vector<int> result(n, 0);
        stack<int> stk;
        for(int i = n-1; i >= 0; i--) {
            while(!stk.empty() && (temperatures[stk.top()] <= temperatures[i])) {
                stk.pop();
            }
            if(!stk.empty()) result[i] = stk.top() - i;
            stk.push(i);
        }
        return result;
    }
};

// Naive Approach:
// For each index i,
// Traverse the index from i+1 to n, to search next greater temperature.

// Time Complexity: O(n^2)
// Space Complexity: O(n)


// Using Stack:
// Iterate through the temperatures in reverse order, starting from the last day.
// Use a stack to keep track of the indices of temperatures.
// For each temperature, compare it with the temperatures in the stack.
// Pop indices from the stack until we find a warmer day or until the stack is empty.
// If the stack is not empty after the while loop: 
// --> There is a warmer day for the current temperature.
// --> Update the result for that day.
// Finally, push the current index onto the stack.

// Time Complexity: O(n)
// Space Complexity: O(n)
