class Solution(object):

    def isSubsequence(self, s, t):
        """
        Given a string s and a string t, check if s is subsequence of t.

        You may assume that there is only lower case English letters in both s and t. t is potentially a very long
        (length ~= 500,000) string, and s is a short string (<=100).

        A subsequence of a string is a new string which is formed from the original string by deleting some (can be
        none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a
        subsequence of "abcde" while "aec" is not).

        14 / 14 test cases passed.
        Status: Accepted
        Runtime: 36 ms
        Memory Usage: 14.1 MB


        Parameters
        ----------
        s : str

        t : str


        Returns
        -------
        ret: bool


        Examples
        --------
        >>> Solution().isSubsequence("abc", "ahbgdc")
        True

        >>> Solution().isSubsequence("axc", "ahbgdc")
        False

        """

        s_idx = 0
        for t_idx in range(len(t)):
            try:
                if t[t_idx] == s[s_idx]:
                    s_idx += 1
            except IndexError:
                return True

        if s_idx is len(s):
            return True
        return False
