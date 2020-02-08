class Solution(object):

    def repeatedSubstringPattern(self, s):
        """
        Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple
        copies of the substring together. You may assume the given string consists of lowercase English letters only and
        its length will not exceed 10000.

        Runtime: 28 ms, faster than 93.09% of Python3 online submissions for Repeated Substring Pattern.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Repeated Substring Pattern.


        Parameters
        ----------
        s : str


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().repeatedSubstringPattern("abab")
        True

        >>> Solution().repeatedSubstringPattern("abcabcabcabc")
        True

        """

        # Lemma 2.3
        return (s + s).index(s, 1) != len(s)

