class Solution(object):

    def toHex(self, num):
        """
        Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method
        is used.

        Note:
        All letters in hexadecimal (a-f) must be in lowercase.
        The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single
        zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
        The given number is guaranteed to fit within the range of a 32-bit signed integer.
        You must not use any method provided by the library which converts/formats the number to hex directly.

        Runtime: 28 ms, faster than 80.91% of Python3 online submissions for Convert a Number to Hexadecimal.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Convert a Number to Hexadecimal.


        Parameters
        ----------
        num : int


        Returns
        -------
        ret : str


        Examples
        --------
        >>> Solution().toHex(26)
        '1A'

        >>> Solution().toHex(-1)
        'ffffffff'

        """

        if num == 0:
            return '0'
        if num < 0:
            num = num - (1 << 32)
            num = num & ((2 ** 32) - 1)

        ret = []
        while num > 0:
            nibble = num % 16
            num = num // 16
            ret.insert(0, str(chr(nibble + 87)) if nibble > 9 else str(nibble))
        return "".join(ret)
