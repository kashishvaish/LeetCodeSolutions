class Solution {
    public int evalRPN(String[] tokens) {
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        Stack<Integer> stack = new Stack<>();
        for(String token: tokens) {
            if(token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/")) {
                int op2 = stack.pop();
                int op1 = stack.pop();
                if(token.equals("+")) {
                    stack.push(op1 + op2);
                } else if(token.equals("-")) {
                    stack.push(op1 - op2);
                } else if(token.equals("*")) {
                    stack.push(op1 * op2);
                } else {
                    stack.push(op1 / op2);
                }
            } else {
                stack.push(Integer.parseInt(token));
            }
        }
        return stack.pop();
    }
}

// Approach:
// Iterate through the list of tokens from left to right.
// If the current token is a number, it is pushed onto the stack.
// If the current token is an operator (+, -, *, /), the top two elements from the stack (operands) are popped and the operation is performed, and the result is pushed back onto the stack.
// The process continues until all tokens are processed, and the final result is the only element remaining in the stack.

// Time Complexity: O(n)
// Space Complexity: O(n)
