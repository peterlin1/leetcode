class Solution(object):
    # Special cycle that all sums lead to if it does not produce 1
    mem = [4, 16, 37, 58, 20, 42, 145, 89]

    def isHappy(self, n):
        """
        Write an algorithm to determine if a number is "happy".

        A happy number is a number defined by the following process: Starting with any positive integer, replace the
        number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will
        stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1
        are happy numbers.

        401 / 401 test cases passed.
        Status: Accepted
        Runtime: 20 ms
        Memory Usage: 13.8 MB


        Parameters
        ----------
        n : int


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().isHappy(19)
        True

        """

        if n is 1:
            return True
        if n in self.mem:
            return False
        return self.isHappy(sum([int(c) ** 2 for c in str(n)]))
