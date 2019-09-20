class MyQueue(object):
    """
    Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.

    Example:

    MyQueue queue = new MyQueue();

    queue.push(1);
    queue.push(2);
    queue.peek();  // returns 1
    queue.pop();   // returns 1
    queue.empty(); // returns false

    Notes:

    You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
    You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

    Runtime: 32 ms, faster than 90.14% of Python3 online submissions for Implement Queue using Stacks.
    Memory Usage: 13.8 MB, less than 10.00% of Python3 online submissions for Implement Queue using Stacks.

    """

    def __init__(self):
        """
        Initialize your data structure here.

        """

        self.data = []
        self.count = 0

    def push(self, x):
        """
        Push element x to the back of queue.


        Parameters
        ----------
        x : int

        """

        self.data.append(x)
        self.count += 1

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.


        Returns
        -------
        ret : int

        """

        if self.count > 0:
            self.count -= 1
            return self.data.pop(0)

    def peek(self):
        """
        Get the front element.


        Returns
        -------
        ret : int

        """

        if self.count > 0:
            return self.data[0]

    def empty(self):
        """
        Returns whether the queue is empty.


        Returns
        -------
        ret : bool

        """

        if self.count == 0:
            return True
        return False
