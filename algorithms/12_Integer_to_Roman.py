class Solution(object):
    val_dict = {1000: 'M',
                500: 'D',
                100: 'C',
                50: 'L',
                10: 'X',
                5: 'V',
                1: 'I'}

    def intToRoman(self, num):
        """
        Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII,
        which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

        Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not
        IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
        The same principle applies to the number nine, which is written as IX. There are six instances where subtraction
        is used:

        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.
        Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

        Runtime: 48 ms, faster than 67.31% of Python3 online submissions for Integer to Roman.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Integer to Roman.


        Parameters
        ----------
        num : int


        Returns
        -------
        ret : str


        Examples
        --------
        >>> Solution().intToRoman(3)
        "III"

        >>> Solution().intToRoman(4)
        "IV"

        >>> Solution().intToRoman(1994)
        "MCMXCIV"

        """

        ret = ""
        pl = 10 ** (len(str(num)) - 1)

        while num != 0:
            digit = num // pl
            if digit is 9:
                ret += self.val_dict[pl] + self.val_dict[int(pl * 10)]
            elif digit >= 5:
                ret += self.val_dict[5 * pl] + (self.val_dict[pl] * (digit - 5))
            elif digit is 4:
                ret += self.val_dict[pl] + self.val_dict[5 * pl]
            else:
                ret += self.val_dict[pl] * digit
            num %= pl
            pl //= 10

        return ret
