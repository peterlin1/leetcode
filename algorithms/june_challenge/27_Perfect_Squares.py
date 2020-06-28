import math


class Solution(object):

    def numSquares(self, n):
        """
        Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...)
        which sum to n.

        Legendre's three-square theorem
        588 / 588 test cases passed.
        Status: Accepted
        Runtime: 28 ms
        Memory Usage: 13.6 MB


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
