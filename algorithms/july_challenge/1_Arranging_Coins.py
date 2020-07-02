import math


class Solution(object):

    def arrangeCoins(self, n):
        """
        You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k
        coins.

        Given n, find the total number of full staircase rows that can be formed.

        n is a non-negative integer and fits within the range of a 32-bit signed integer.

        1336 / 1336 test cases passed.
        Status: Accepted
        Runtime: 36 ms
        Memory Usage: 13.8 MB


        Parameters
        ----------
        n : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().arrangeCoins(5)
        2

        >>> Solution().arrangeCoins(8)
        3

        """

        return math.floor(-0.5 + math.sqrt(2 * n + 0.25))
