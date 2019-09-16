class MyStack(object):
    """
    Implement the following operations of a stack using queues.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    empty() -- Return whether the stack is empty.
    Example:

    MyStack stack = new MyStack();

    stack.push(1);
    stack.push(2);
    stack.top();   // returns 2
    stack.pop();   // returns 2
    stack.empty(); // returns false

    Notes:

    You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is
    empty operations are valid.
    Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque
    (double-ended queue), as long as you use only standard operations of a queue.
    You may assume that all operations are valid (for example, no pop or top operations will be called on an empty
    stack).

    Runtime: 36 ms, faster than 66.00% of Python3 online submissions for Implement Stack using Queues.
    Memory Usage: 13.8 MB, less than 20.00% of Python3 online submissions for Implement Stack using Queues.

    """

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.data = []
        self.count = 0

    def push(self, x):
        """

        Parameters
        ----------
        x : int

        """

        self.data.append(x)
        self.count += 1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.


        Returns
        -------
        ret : int

        """

        if self.count > 0:
            self.count -= 1
            return self.data.pop(-1)

    def top(self):
        """
        Get the top element.


        Returns
        -------
        ret : int

        """
        if self.count > 0:
            return self.data[-1]

    def empty(self):
        """
        Returns whether the stack is empty.


        Returns
        -------
        ret : bool

        """

        if self.count == 0:
            return True
        return False
