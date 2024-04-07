class Solution:
    def checkValidString(self, s: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        o = 0
        c = 0
        n = len(s)
        for i in range(n):
            j = n-1-i
            if s[i] == "(" or s[i] == "*": o += 1
            else: o -= 1
            if s[j] == ")" or s[j] == "*": c += 1
            else: c -=1
            if o < 0 or c < 0: return False
        return True

# Approach:
# Initialize two variables o and c to keep track of the counts of open and close parentheses, respectively, starting from 0.
# Obtain the length of the input string s and store it in the variable n.
# Iterate through each character of the string s using a for loop, with index i ranging from 0 to n-1.
# For each character at index i, and its corresponding character at index n-1-i (using two separate indices):
# If the character at index i is an open parenthesis "(" or a wildcard "*", increment the count of open parentheses o by 1.
# If the character at index n-1-i is a close parenthesis ")" or a wildcard "*", increment the count of close parentheses c by 1.
# If the character at index i is a close parenthesis ")" or a wildcard "*", decrement the count of open parentheses o by 1.
# If the character at index n-1-i is an open parenthesis "(" or a wildcard "*", decrement the count of close parentheses c by 1.
# During each iteration, if at any point the count of open parentheses o or close parentheses c becomes negative, it means there are more close parentheses than open parentheses at that point, violating the balance of parentheses. In such cases, return False.
# If the loop completes without encountering any violations, return True, indicating that the string is valid.
    
# Time Complexity: O(n)
# Space Complexity: O(1)
