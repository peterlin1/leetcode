class MinStack(object):
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.


    Example:

    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> Returns -3.
    minStack.pop();
    minStack.top();      --> Returns 0.
    minStack.getMin();   --> Returns -2.

    Runtime: 68 ms, faster than 90.88% of Python3 online submissions for Min Stack.
    Memory Usage: 17.7 MB, less than 5.36% of Python3 online submissions for Min Stack.

    """

    def __init__(self):
        self.data = []
        self.length = 0

    def push(self, x):
        """
        Push element x onto stack.

        Parameters
        ----------
        x : int

        """
        if self.length == 0:
            self.data.append((x, x))
        else:
            self.data.append((x, min(x, self.data[-1][1])))
        self.length += 1

    def pop(self):
        """
        Removes the element on top of the stack.

        """
        if self.length > 0:
            self.data.pop()
            self.length -= 1

    def top(self):
        """
        Get the top element.


        Returns
        -------
        ret : int

        """
        if self.length > 0:
            return self.data[-1][0]

    def getMin(self):
        """
        Retrieve the minimum element in the stack.


        Returns
        -------
        ret : int

        """
        if self.length > 0:
            return self.data[-1][1]


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
