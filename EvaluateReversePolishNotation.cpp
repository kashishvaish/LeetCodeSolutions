class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        stack<int> stk;
        for(string token: tokens) {
            if(token == "+" || token == "-" || token == "*" || token == "/") {
                int op2 = stk.top();
                stk.pop();
                int op1 = stk.top();
                stk.pop();
                if(token == "+") {
                    stk.push(op1 + op2);
                } else if(token == "-") {
                    stk.push(op1 - op2);
                } else if(token == "*") {
                    stk.push(op1 * op2);
                } else {
                    stk.push(op1 / op2);
                }
            } else {
                stk.push(stoi(token));
            }
        }
        return stk.top();
    }
};

// Approach:
// Iterate through the list of tokens from left to right.
// If the current token is a number, it is pushed onto the stack.
// If the current token is an operator (+, -, *, /), the top two elements from the stack (operands) are popped and the operation is performed, and the result is pushed back onto the stack.
// The process continues until all tokens are processed, and the final result is the only element remaining in the stack.

// Time Complexity: O(n)
// Space Complexity: O(n)
