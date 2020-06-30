import operator
from functools import reduce


class Solution(object):

    def uniquePaths(self, m, n):
        """
        A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

        The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right
        corner of the grid (marked 'Finish' in the diagram below).

        How many possible unique paths are there?

        Mathematical solution
        https://betterexplained.com/articles/navigate-a-grid-using-combinations-and-permutations/

        62 / 62 test cases passed.
        Status: Accepted
        Runtime: 32 ms
        Memory Usage: 13.9 MB


        Parameters
        ----------
        m : int

        n : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().uniquePaths(3, 2)
        3

        >>> Solution().uniquePaths(7, 3)
        28

        """

        def ncr(num, r):
            r = min(r, num - r)
            numer = reduce(operator.mul, range(num, num - r, -1), 1)
            denom = reduce(operator.mul, range(1, r + 1), 1)
            return numer // denom

        return ncr(m + n - 2, m - 1)

