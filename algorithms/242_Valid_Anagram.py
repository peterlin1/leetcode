class Solution(object):

    def isAnagram(self, s, t):
        """
        Given two strings s and t , write a function to determine if t is an anagram of s.


        Parameters
        ----------
        s : str
        t : str


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().isAnagram("anagram", "nagaram")
        True

        >>> Solution().isAnagram("rat", "car")
        False

        >>> Solution().isAnagram("aa", "bb")
        False

        >>> Solution().isAnagram("ac", "bb")
        False

        >>> Solution().isAnagram("ad", "bb")
        False

        >>> Solution().isAnagram("xaaddy", "xbbccy")
        False

        """

        if len(s) != len(t):
            return False

        if sorted(s) != sorted(t):
            return False
        return True
