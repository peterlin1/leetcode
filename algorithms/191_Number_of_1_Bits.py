class Solution(object):

    def hammingWeight(self, n):
        """
        Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the
        Hamming weight).

        Runtime: 16 ms, faster than 77.96% of Python online submissions for Number of 1 Bits.
        Memory Usage: 11.7 MB, less than 62.50% of Python online submissions for Number of 1 Bits.


        Parameters
        ----------
        n : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().hammingWeight(11)
        3

        """

        ret = 0
        while n != 0:
            if n % 2 == 1:
                ret += 1
            n = n // 2
        return ret
