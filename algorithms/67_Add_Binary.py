class Solution(object):

    def addBinary(self, a, b):
        """
        Given two binary strings, return their sum (also a binary string).

        The input strings are both non-empty and contains only characters 1 or 0.

        Runtime: 48 ms, faster than 18.75% of Python3 online submissions for Add Binary.
        Memory Usage: 13.8 MB, less than 5.41% of Python3 online submissions for Add Binary.


        Parameters
        ----------
        a : str
        b : str


        Returns
        -------
        ret : str


        Examples
        --------
        >>> Solution().addBinary("1010", "1011")
        '10101'

        """
        a = a[::-1]
        b = b[::-1]
        ret = ""
        rem = 0
        for idx in range(max(len(a), len(b))):
            try:
                a_val = int(a[idx])
            except IndexError:
                a_val = 0

            try:
                b_val = int(b[idx])
            except IndexError:
                b_val = 0

            s_sum = a_val + b_val + rem
            ret = ret + str(s_sum % 2)
            rem = s_sum // 2
        if rem > 0:
            ret = ret + str(rem)
        return ret[::-1]
