import math

class Solution(object):
    def isUgly(self, num):
        """
        Write a program to check whether a given number is an ugly number.

        Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

        Note:

        1 is typically treated as an ugly number.
        Input is within the 32-bit signed integer range: [−231,  231 − 1].

        Runtime: 44 ms, faster than 21.11% of Python3 online submissions for Ugly Number.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Ugly Number.
        Next challenges:


        Parameters
        ----------
        num : int


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().isUgly(6)
        True

        >>> Solution().isUgly(8)
        True

        >>> Solution().isUgly(14)
        False

        """

        if num < 1:
            return False

        for i in [2, 3, 5]:
            while num % i == 0:
                num = num / i

        if num > 1:
            return False
        return True
