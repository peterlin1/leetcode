class Solution(object):

    def longestPalindrome(self, s):
        """
        Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is
        1000.

        Runtime: 952 ms, faster than 77.58% of Python3 online submissions for Longest Palindromic Substring.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Palindromic Substring.


        Parameters
        ----------
        s : str


        Returns
        -------
        ret : str


        Examples
        --------
        >>> Solution().longestPalindrome("babad")
        "bab"

        >>> Solution().longestPalindrome("cbbd")
        bb

        """

        ret = ""

        def _iterate(start_idx, end_idx):
            while start_idx >= 0 and end_idx < len(s) and s[start_idx] == s[end_idx]:
                start_idx -= 1
                end_idx += 1
            if end_idx - start_idx - 1 > len(ret):
                return s[start_idx + 1: end_idx]
            return ret

        for idx in range(len(s)):
            ret = _iterate(idx, idx)
            ret = _iterate(idx, idx + 1)

        return ret
