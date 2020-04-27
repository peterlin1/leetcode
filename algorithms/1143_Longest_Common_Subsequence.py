class Solution(object):

    def longestCommonSubsequence(self, text1, text2):
        """
        Given two strings text1 and text2, return the length of their longest common subsequence.

        A subsequence of a string is a new string generated from the original string with some characters(can be none)
        deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde"
        while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

        If there is no common subsequence, return 0.

        Constraints:

        1 <= text1.length <= 1000
        1 <= text2.length <= 1000
        The input strings consist of lowercase English characters only.

        Runtime: 592 ms, faster than 31.01% of Python3 online submissions for Longest Common Subsequence.
        Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Longest Common Subsequence.


        Parameters
        ----------
        text1 : str

        text2 : str


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().longestCommonSubsequence("abcde", "ace")
        3

        >>> Solution().longestCommonSubsequence("abc", "abc")
        3

        >>> Solution().longestCommonSubsequence("abc", "def")
        0

        """

        if len(text1) < len(text2):
            return self.longestCommonSubsequence(text2, text1)

        mem = [0] * (len(text2) + 1)
        for idx in range(1, len(text1) + 1):
            k = 0
            for jdx in range(1, len(text2) + 1):
                if text1[idx - 1] == text2[jdx - 1]:
                    mem[jdx] = k + 1
                else:
                    k = mem[jdx]
                    mem[jdx] = max(mem[jdx - 1], k)
        return mem[-1]
