import re

class Solution(object):

    def myAtoi(self, str):
        """
        Implement atoi which converts a string to an integer.

        The function first discards as many whitespace characters as necessary until the first non-whitespace character
        is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many
        numerical digits as possible, and interprets them as a numerical value.

        The string can contain additional characters after those that form the integral number, which are ignored and
        have no effect on the behavior of this function.

        If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence
        exists because either str is empty or it contains only whitespace characters, no conversion is performed.

        If no valid conversion could be performed, a zero value is returned.

        Note:

        Only the space character ' ' is considered as whitespace character.
        Assume we are dealing with an environment which could only store integers within the 32-bit signed integer
        range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1)
        or INT_MIN (−231) is returned.

        Runtime: 32 ms, faster than 68.84% of Python3 online submissions for String to Integer (atoi).
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for String to Integer (atoi).


        Parameters
        ----------
        str : str


        Returns
        -------

        """

        sb = re.search(r"""^\s*([\+-]?\d+)""", str)
        if not sb:
            return 0

        ret = int(sb.groups()[0])
        if ret > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if ret < -(2 ** 31):
            return -(2 ** 31)
        return ret
