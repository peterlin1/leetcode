class Solution:

    def reverseBits(self, n):
        """
        Reverse bits of a given 32 bits unsigned integer.

        Runtime: 8 ms, faster than 99.08% of Python online submissions for Reverse Bits.
        Memory Usage: 11.7 MB, less than 57.14% of Python online submissions for Reverse Bits.


        Parameters
        ----------
        n : int

        Returns
        -------
        ret : int

        Examples
        --------
        >>> Solution().reverseBits(43261596)
        964176192

        >>> Solution().reverseBits(4294967293)
        3221225471

        """

        b_n = '{:032b}'.format(n)
        b_n_r = b_n[::-1]
        return int(b_n_r, 2)
