class Solution(object):

    def trailingZeroes(self, n):
        """
        Given an integer n, return the number of trailing zeroes in n!.

        Runtime: 32 ms, faster than 93.51% of Python3 online submissions for Factorial Trailing Zeroes.
        Memory Usage: 13.8 MB, less than 10.00% of Python3 online submissions for Factorial Trailing Zeroes.


        Parameters
        ----------
        n : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().trailingZeroes(191)
        46

        >>> Solution().trailingZeroes(5)
        1

        >>> Solution().trailingZeroes(3)
        0

        """

        # Similar to base base-conversion division. Number of trailing zeroes is equal to the sum of quotients of n
        # divided by powers of 5.
        ret = 0
        while n != 0:
            q_n = n // 5
            ret += q_n
            n = q_n
        return ret
