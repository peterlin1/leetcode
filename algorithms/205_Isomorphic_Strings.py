class Solution(object):

    def isIsomorphic(self, s, t):
        """
        Given two strings s and t, determine if they are isomorphic.

        Two strings are isomorphic if the characters in s can be replaced to get t.

        All occurrences of a character must be replaced with another character while preserving the order of characters.
        No two characters may map to the same character but a character may map to itself.

        Runtime: 48 ms, faster than 56.23% of Python3 online submissions for Isomorphic Strings.
        Memory Usage: 14 MB, less than 17.50% of Python3 online submissions for Isomorphic Strings.


        Parameters
        ----------
        s : str

        t : str


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().isIsomorphic(s="egg", t="add")
        True

        >>> Solution().isIsomorphic(s="aa", t="ab")
        False

        >>> Solution().isIsomorphic(s="paper", t="title")
        True

        """
        mem = {}
        r_mem = {}
        for idx in range(len(s)):
            try:
                if mem[s[idx]] != t[idx]:
                    return False
            except KeyError:
                pass

            try:
                if r_mem[t[idx]] != s[idx]:
                    return False
            except KeyError:
                pass
            mem[s[idx]] = t[idx]
            r_mem[t[idx]] = s[idx]
        return True
