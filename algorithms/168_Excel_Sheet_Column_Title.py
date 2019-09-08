class Solution(object):

    def convertToTitle(self, n):
        """
        Given a positive integer, return its corresponding column title as appear in an Excel sheet.

        Base 26 (Hexavigesimal) Cipher

        Runtime: 36 ms, faster than 62.29% of Python3 online submissions for Excel Sheet Column Title.
        Memory Usage: 13.8 MB, less than 6.25% of Python3 online submissions for Excel Sheet Column Title.


        Parameters
        ----------
        n : int


        Returns
        -------
        ret : str


        Examples
        --------
        >>> Solution().convertToTitle(1)
        'A'

        >>> Solution().convertToTitle(28)
        'AB'

        >>> Solution().convertToTitle(701)
        'ZY'

        >>> Solution().convertToTitle(702)
        'ZZ'

        >>> Solution().convertToTitle(1083481)
        'BIPTI'

        """

        d2t = ""
        if n == 0:
            return d2t
        while n > 0:
            if n % 26 == 0:
                d2t = 'Z' + d2t
                n = (n // 26) - 1
            else:
                d2t = chr((n % 26) + 64) + d2t
                n = n // 26
        return d2t
