class Solution(object):

    def checkInclusion(self, s1, s2):
        """
        Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other
        words, one of the first string's permutations is the substring of the second string.

        Runtime: 56 ms, faster than 95.97% of Python3 online submissions for Permutation in String.
        Memory Usage: 13.8 MB, less than 8.33% of Python3 online submissions for Permutation in String.


        Parameters
        ----------
        s1 : str

        s2 : str


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().checkInclusion("ab", "eidbaooo")
        True

        >>> Solution().checkInclusion("ab", "eidboaoo")
        False

        """

        if len(s1) > len(s2):
            return False

        _s1 = [0] * 26
        _s2 = [0] * 26

        for char in s1:
            _s1[ord(char) - 97] += 1

        for char in s2[:len(s1)]:
            _s2[ord(char) - 97] += 1

        if _s1 == _s2:
            return True

        _head_s2 = 0
        for idx in range(len(s1), len(s2)):
            _s2[ord(s2[idx]) - 97] += 1
            _s2[ord(s2[_head_s2]) - 97] -= 1
            if _s2 == _s1:
                return True
            _head_s2 += 1
        return False
