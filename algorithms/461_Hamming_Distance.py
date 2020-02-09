class Solution(object):

    def hammingDistance(self, x, y):
        """
        The Hamming distance between two integers is the number of positions at which the corresponding bits are
        different.

        Given two integers x and y, calculate the Hamming distance.

        Runtime: 28 ms, faster than 65.23% of Python3 online submissions for Hamming Distance.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Hamming Distance.


        Parameters
        ----------
        x : int

        y : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().hammingDistance(1, 4)
        2

        """

        b_and = x ^ y
        ret = 0
        while b_and != 0:
            ret += b_and & 1
            b_and >>= 1
        return ret
