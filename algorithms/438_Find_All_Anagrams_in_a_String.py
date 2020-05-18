class Solution(object):

    def findAnagrams(self, s, p):
        """
        Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

        Strings consists of lowercase English letters only and the length of both strings s and p will not be larger
        than 20,100.

        The order of output does not matter.

        Runtime: 80 ms, faster than 97.67% of Python3 online submissions for Find All Anagrams in a String.
        Memory Usage: 14.9 MB, less than 8.70% of Python3 online submissions for Find All Anagrams in a String.


        Parameters
        ----------
        s : str

        p : str


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().findAnagrams("cbaebabacd", "abc")
        [0, 6]

        >>> Solution().findAnagrams("abab", "ab")
        [0, 1, 2]

        """

        ret = []
        if len(p) > len(s):
            return ret

        _s = [0] * 26
        _p = [0] * 26

        for char in p:
            _p[ord(char) - 97] += 1

        for char in s[:len(p)]:
            _s[ord(char) - 97] += 1

        if _s == _p:
            ret.append(0)

        pointer = 0
        for idx in range(len(p), len(s)):
            _s[ord(s[idx]) - 97] += 1
            _s[ord(s[pointer]) - 97] -= 1
            if _s == _p:
                ret.append(pointer + 1)
            pointer += 1
        return ret
