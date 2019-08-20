class Solution(object):
    def isValid(self, s):
        """
        Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Note that an empty string is also considered valid.

        Runtime: 52 ms, faster than 11.43% of Python3 online submissions for Valid Parentheses.
        Memory Usage: 13.8 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.


        Parameters
        ----------
        s : str


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().isValid("{[]}")
        True

        >>> Solution().isValid("([)]")
        False

        """

        s_l = len(s)
        while len(s) is not 0:
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
            if s_l == len(s):
                return False
            else:
                s_l = len(s)
        return True
