class Solution(object):

    def findLUSlength(self, a, b):
        """
        Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings.
        The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this
        subsequence should not be any subsequence of the other strings.

        A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing
        the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a
        subsequence of any string.

        The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the
        longest uncommon subsequence doesn't exist, return -1.

        Runtime: 28 ms, faster than 55.91% of Python3 online submissions for Longest Uncommon Subsequence I .
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Uncommon Subsequence I .


        Parameters
        ----------
        a : str

        b : str


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().findLUSlength("aba", "cdc")
        3

        """

        return max(len(a), len(b)) if a != b else -1
