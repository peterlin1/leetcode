

class Solution(object):

    def isPalindrome(self, x):
        """
        Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as
        forward.

        Runtime: 72 ms, faster than 61.66% of Python3 online submissions for Palindrome Number.
        Memory Usage: 13.7 MB, less than 6.50% of Python3 online submissions for Palindrome Number.


        Parameters
        ----------
        x : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().isPalindrome(121)
        True

        >>> Solution().isPalindrome(-121)
        False

        """

        if x < 0:
            return False
        if x == int(str(x)[::-1]):
            return True
        else:
            return False

