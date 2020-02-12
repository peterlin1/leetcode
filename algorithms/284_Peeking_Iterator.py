# Below is the interface for Iterator, which is already defined for you.


class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.

        Parameters
        ----------
        nums : list

        """
        pass

    def hasNext(self):
        """
        Returns true if the iteration has more elements.

        Returns
        -------
        bool

        """
        pass

    def next(self):
        """
        Returns the next element in the iteration.

        Returns
        -------
        int

        """
        pass


class PeekingIterator(object):
    """
    Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that
    support the peek() operation -- it essentially peek() at the element that will be returned by the next call to
    next().

    Your PeekingIterator object will be instantiated and called as such:
    iter = PeekingIterator(Iterator(nums))
    while iter.hasNext():
    val = iter.peek()   # Get the next element but not advance the iterator.
    iter.next()         # Should return the same value as [val].

    Runtime: 24 ms, faster than 95.32% of Python3 online submissions for Peeking Iterator.
    Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Peeking Iterator.

    """

    def __init__(self, iterator):
        """
        Initialize your data structure here.

        Parameters
        ----------
        iterator : Iterator

        """

        self.it = iterator
        self._next = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self._next is not None:
            return self._next

        if self.it.hasNext():
            self._next = self.it.next()
            return self._next
        return None

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            raise Exception('No next element')

        _next = self._next
        self._next = None
        return _next

    def hasNext(self):
        """
        :rtype: bool
        """
        if self._next is not None:
            return True

        if self.it.hasNext():
            self._next = self.it.next()
            return True

        return False
