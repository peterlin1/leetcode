import re


class Solution(object):

    def isPalindrome(self, s):
        """
        Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

        Note: For the purpose of this problem, we define empty string as valid palindrome.

        Runtime: 48 ms, faster than 89.30% of Python3 online submissions for Valid Palindrome.
        Memory Usage: 15 MB, less than 9.52% of Python3 online submissions for Valid Palindrome.


        Parameters
        ----------
        s : str


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().isPalindrome("A man, a plan, a canal: Panama")
        True

        >>> Solution().isPalindrome("race a car")
        False

        """

        if s == "":
            return True
        s = re.sub(r'\W+', '', s).lower()
        for c in range(len(s) // 2):
            if s[c] != s[-1 - c]:
                return False
        return True
