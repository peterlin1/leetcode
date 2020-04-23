class Solution(object):

    def rangeBitwiseAnd(self, m, n):
        """
        Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range,
        inclusive.

        Runtime: 52 ms, faster than 82.23% of Python3 online submissions for Bitwise AND of Numbers Range.
        Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Bitwise AND of Numbers Range.


        Parameters
        ----------
        m : int

        n : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().rangeBitwiseAnd([5, 7])
        4

        >>> Solution().rangeBitwiseAnd([0, 1])
        0

        """

        while m < n:
            n -= (n & -n)
        return n
