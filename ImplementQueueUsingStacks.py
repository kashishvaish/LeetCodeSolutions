class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # Time Complexity: O(1)
        self.stack1.append(x)

    def pop(self) -> int:
        # Time Complexity: Amortized O(1); Worst case O(n)
        if not self.stack1 and not self.stack2: return 
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
             

    def peek(self) -> int:
        # Time Complexity: Amortized O(1); Worst case O(n)
        if not self.stack1 and not self.stack2: return 
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        # Time Complexity: O(1)
        return not self.stack1 and not self.stack2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Approach 1: Push - O(n) and Pop - O(1)
# Push Operation - Transfer all stack1 elements to auxiliary stack stack2. Push the new element in stack1 and pop all the elements from stack2 back to stack1.
# Pop Operation - Pop the topmost element in stack1.

# Code:
# class MyQueue:

#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []

#     def push(self, x: int) -> None:
#         # Time Complexity: O(n)
#         while self.stack1:
#             self.stack2.append(self.stack1.pop())
#         self.stack1.append(x)
#         while self.stack2:
#             self.stack1.append(self.stack2.pop())

#     def pop(self) -> int:
#         # Time Complexity: O(1)
#         if self.stack1 != []:
#             return self.stack1.pop()

#     def peek(self) -> int:
#         # Time Complexity: O(1)
#         if self.stack1 != []:
#             return self.stack1[-1]

#     def empty(self) -> bool:
#         # Time Complexity: O(1)
#         return self.stack1 == []

# Approach 2: Push - O(1) and Pop - Amortized O(1)
# Push Operation - Add element in stack1
# Pop Operation -
#   1. If both stack1 and stack2 are empty --> return
#   2. It stack2 is empty --> pop all elements from stack1 to stack2
#   3. Pop the top element from stack2

# Code:
# class MyQueue:

#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []

#     def push(self, x: int) -> None:
#         # Time Complexity: O(1)
#         self.stack1.append(x)

#     def pop(self) -> int:
#         # Time Complexity: Amortized O(1); Worst case O(n)
#         if not self.stack1 and not self.stack2: return 
#         if not self.stack2:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#         return self.stack2.pop()
             

#     def peek(self) -> int:
#         # Time Complexity: Amortized O(1); Worst case O(n)
#         if not self.stack1 and not self.stack2: return 
#         if not self.stack2:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#         return self.stack2[-1]

#     def empty(self) -> bool:
#         # Time Complexity: O(1)
#         return not self.stack1 and not self.stack2
