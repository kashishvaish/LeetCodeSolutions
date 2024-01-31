class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        int n = temperatures.length;
        int[] result = new int[n];
        Stack<Integer> stack = new Stack<>();
        for(int i = n-1; i >= 0; i--) {
            while(!stack.empty() && (temperatures[stack.peek()] <= temperatures[i])) {
                stack.pop();
            }
            if(!stack.empty()) {
                result[i] = stack.peek() - i;
            }
            stack.push(i);
        }
        return result;
    }
}

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
