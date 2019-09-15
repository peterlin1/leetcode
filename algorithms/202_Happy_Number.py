class Solution(object):

    def isHappy(self, n):
        """
        Write an algorithm to determine if a number is "happy".

        A happy number is a number defined by the following process: Starting with any positive integer, replace the
        number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will
        stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1
        are happy numbers.

        Runtime: 40 ms, faster than 75.75% of Python3 online submissions for Happy Number.
        Memory Usage: 13.7 MB, less than 5.26% of Python3 online submissions for Happy Number.


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
        mem = []
        while n != 1:
            if n in mem:
                return False
            mem.append(n)
            s_n = str(n)
            s_n_c = 0
            for c in s_n:
                s_n_c += int(c) ** 2
            n = s_n_c
        return True
