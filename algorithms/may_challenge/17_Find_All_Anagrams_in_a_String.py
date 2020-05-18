class Solution(object):

    def findAnagrams(self, s, p):
        """
        Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

        Strings consists of lowercase English letters only and the length of both strings s and p will not be larger
        than 20,100.

        The order of output does not matter.

        36 / 36 test cases passed.
        Status: Accepted
        Runtime: 84 ms
        Memory Usage: 15 MB


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

        _head_s = 0
        for idx in range(len(p), len(s)):
            _s[ord(s[idx]) - 97] += 1
            _s[ord(s[_head_s]) - 97] -= 1
            if _s == _p:
                ret.append(_head_s + 1)
            _head_s += 1
        return ret
