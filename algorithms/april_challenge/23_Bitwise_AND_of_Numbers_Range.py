class Solution(object):

    def rangeBitwiseAnd(self, m, n):
        """
        Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range,
        inclusive.

        8266 / 8266 test cases passed.
        Status: Accepted
        Runtime: 52 ms
        Memory Usage: 13.8 MB


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
