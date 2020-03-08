class Solution(object):

    def judgeSquareSum(self, c):
        """
        Given a non-negative integer c, your task is to decide whether there're two integers a and b such that
        a2 + b2 = c.

        Runtime: 388 ms, faster than 18.39% of Python3 online submissions for Sum of Square Numbers.
        Memory Usage: 16.6 MB, less than 50.00% of Python3 online submissions for Sum of Square Numbers.


        Parameters
        ----------
        c : int


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().judgeSquareSum(5)
        True

        >>> Solution().judgeSquareSum(3)
        False

        """

        mem = set()
        for dg in range(int(c ** 0.5) + 1):
            mem.add(c - (dg ** 2))
            if (dg ** 2) in mem:
                return True
        return False
