class Solution(object):

    def getSum(self, a, b):
        """
        Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

        Runtime: 28 ms, faster than 87.90% of Python3 online submissions for Sum of Two Integers.
        Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Sum of Two Integers.


        Parameters
        ----------
        a : int

        b : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().getSum(1, 2)
        3

        >>> Solution().getSum(-2, 3)
        1

        """

        while a & 0xffffffff:
            c = a & b
            b ^= a
            a = c << 1
        if a > 0xffffffff:
            return b & 0xffffffff
        return b
