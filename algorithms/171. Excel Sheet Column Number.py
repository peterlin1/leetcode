class Solution(object):

    def titleToNumber(self, s):
        """
        Given a column title as appear in an Excel sheet, return its corresponding column number.

        Runtime: 32 ms, faster than 95.71% of Python3 online submissions for Excel Sheet Column Number.
        Memory Usage: 14 MB, less than 9.09% of Python3 online submissions for Excel Sheet Column Number.


        Parameters
        ----------
        s : str


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().titleToNumber('A')
        1

        >>> Solution().titleToNumber('AB')
        28

        >>> Solution().titleToNumber('ZY')
        701

        >>> Solution().titleToNumber('ZZ')
        702

        >>> Solution().titleToNumber('BIPTI')
        1083481

        """
        ret = 0
        for idx, col in enumerate(s[::-1]):
            h_bit = (ord(col) - 64)
            ret += h_bit * 26 ** idx
        return ret
