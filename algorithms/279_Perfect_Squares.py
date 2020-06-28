import math


class Solution(object):

    def numSquares(self, n):
        """
        Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...)
        which sum to n.

        Legendre's three-square theorem
        Runtime: 44 ms, faster than 97.26% of Python3 online submissions for Perfect Squares.
        Memory Usage: 14 MB, less than 55.99% of Python3 online submissions for Perfect Squares.


        Parameters
        ----------
        n : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().numSquares(12)
        3

        >>> Solution().numSquares(13)
        2

        """

        def _square(num):
            sr_n = math.sqrt(num)
            return int(sr_n + 0.5) ** 2 == num

        if _square(n):
            return 1

        while (n & 3) == 0:
            n >>= 2

        if (n & 7) == 7:
            return 4

        for i in range(1, int(math.sqrt(n)) + 1):
            if _square(n - i * i):
                return 2

        return 3
