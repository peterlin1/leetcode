class Solution(object):

    def longestPalindrome(self, s):
        """
        Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that
        can be built with those letters.

        This is case sensitive, for example "Aa" is not considered a palindrome here.

        Note:
        Assume the length of given string will not exceed 1,010.

        Runtime: 36 ms, faster than 68.70% of Python3 online submissions for Longest Palindrome.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Palindrome.


        Parameters
        ----------
        s : str


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().longestPalindrome('abccccdd')
        7

        """

        ret = 0
        mem = {}
        for char in s:
            try:
                cnt = mem[char] + 1
            except KeyError:
                cnt = 1

            if cnt is 2:
                ret += 2
            mem[char] = cnt % 2

        if 1 in mem.values():
            ret += 1
        return ret
