class Solution(object):

    def arrangeCoins(self, n):
        """
        You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k
        coins.

        Given n, find the total number of full staircase rows that can be formed.

        n is a non-negative integer and fits within the range of a 32-bit signed integer.

        Runtime: 852 ms, faster than 42.26% of Python3 online submissions for Arranging Coins.
        Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Arranging Coins.


        Parameters
        ----------
        n

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

        ret = 0
        while n > 0:
            ret += 1
            n -= ret
        if n is 0:
            return ret
        return ret - 1
