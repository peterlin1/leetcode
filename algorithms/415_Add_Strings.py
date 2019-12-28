class Solution(object):

    def addStrings(self, num1, num2):
        """
        Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

        Note:
        The length of both num1 and num2 is < 5100.
        Both num1 and num2 contains only digits 0-9.
        Both num1 and num2 does not contain any leading zero.
        You must not use any built-in BigInteger library or convert the inputs to integer directly.

        Runtime: 36 ms, faster than 89.66% of Python3 online submissions for Add Strings.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Add Strings.


        Parameters
        ----------
        num1 : str

        num2 : str


        Returns
        -------
        ret : str


        Examples
        --------
        >>> Solution().addStrings("1", "2")
        '3'

        """

        if len(num1) > len(num2):
            l_l = len(num1)
        else:
            l_l = len(num2)
            t_n = num1
            num1 = num2
            num2 = t_n

        ret = ""
        carry = 0
        for idx in range(-1, -1 * l_l - 1, -1):
            try:
                s = int(num1[idx]) + int(num2[idx]) + carry
            except IndexError:
                s = int(num1[idx]) + carry

            if s > 9:
                carry = 1
                s = s % 10
            else:
                carry = 0
            ret = str(s) + ret

        if carry == 1:
            return "1" + ret
        return ret
