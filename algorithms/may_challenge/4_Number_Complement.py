class Solution(object):

    def findComplement(self, num):
        """
        Given a positive integer, output its complement number. The complement strategy is to flip the bits of its
        binary representation.

        Note:
        The given integer is guaranteed to fit within the range of a 32-bit signed integer.
        You could assume no leading zero bit in the integer’s binary representation.


        149 / 149 test cases passed.
        Status: Accepted
        Runtime: 24 ms
        Memory Usage: 13.8 MB


        Parameters
        ----------
        num : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().findComplement(5)
        2

        >>> Solution().findComplement(1)
        0

        """

        n_bits = 0
        n_num = num
        while n_num != 0:
            n_num >>= 1
            n_bits += 1
        return ((1 << n_bits) - 1) ^ num
