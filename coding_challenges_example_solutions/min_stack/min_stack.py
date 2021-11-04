"""
Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
  void push(int val) pushes the element val onto the stack.
  void pop() removes the element on the top of the stack.
  int top() gets the top element of the stack.
  int getMin() retrieves the minimum element in the stack.
"""


class MinStack:    
    def __init__(self):
        self.stack = []
        self.minIxSt = []

    def push(self, val):
        self.stack.append(val)
        if len(self.minIxSt) == 0:
            self.minIxSt.append(len(self.stack) - 1)
        else:
            if val < self.stack[self.minIxSt[-1]]:
                self.minIxSt.append(len(self.stack) - 1)

    def pop(self):        
        if len(self.stack) - 1 == self.minIxSt[-1]:
            self.minIxSt.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.stack[self.minIxSt[-1]]


Mst = MinStack()
Mst.push(9)
Mst.push(10)
Mst.push(3)
Mst.pop()
print(Mst.getMin())
print(Mst.top())
