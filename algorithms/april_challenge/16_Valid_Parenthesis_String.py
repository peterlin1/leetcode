class Solution(object):

    def checkValidString(self, s):
        """
        Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether
        this string is valid. We define the validity of a string by these rules:

        Any left parenthesis '(' must have a corresponding right parenthesis ')'.
        Any right parenthesis ')' must have a corresponding left parenthesis '('.
        Left parenthesis '(' must go before the corresponding right parenthesis ')'.
        '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
        An empty string is also valid.

        Note:
        The string size will be in the range [1, 100].

        58 / 58 test cases passed.
        Status: Accepted
        Runtime: 28 ms
        Memory Usage: 13.9 MB

        Parameters
        ----------
        s : str


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().checkValidString("()")
        True

        >>> Solution().checkValidString("(*)")
        True

        >>> Solution().checkValidString("(*))")
        True

        """

        open_b = [0, 0]

        for char in s:
            if char == '(':
                open_b[0] += 1
            else:
                open_b[0] -= 1

            if char != ')':
                open_b[1] += 1
            else:
                open_b[1] -= 1

            if open_b[1] < 0:
                return False
            open_b[0] = max(open_b[0], 0)

        return open_b[0] == 0
