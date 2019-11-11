class Solution(object):

    def addDigits(self, num):
        """
        Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

        Runtime: 20 ms, faster than 99.96% of Python3 online submissions for Add Digits.
        Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Add Digits.


        Parameters
        ----------
        num : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().addDigits(38)
        2

        """

        if num is 0:
            return 0
        if num % 9 is 0:
            return 9
        return num % 9
