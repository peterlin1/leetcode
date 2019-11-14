class Solution(object):
    def wordPattern(self, pattern, str):
        """
        Given a pattern and a string str, find if str follows the same pattern.

        Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word
        in str.

        Runtime: 28 ms, faster than 95.99% of Python3 online submissions for Word Pattern.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Word Pattern.


        Parameters
        ----------
        pattern : str

        str : str


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().wordPattern("abba", "dog cat cat dog")
        True

        >>> Solution().wordPattern("abba", "dog cat cat fish")
        False

        >>> Solution().wordPattern("abba", "dog dog dog dog")
        False

        >>> Solution().wordPattern("abba", "dog cat cat dog rabbit")
        False

        """

        s_l = str.split()
        if len(s_l) != len(pattern):
            return False

        w_dict = {}
        rw_dict = {}
        for idx, val in enumerate(s_l):
            try:
                if w_dict[pattern[idx]] != val:
                    return False
            except KeyError:
                w_dict[pattern[idx]] = val

            try:
                if rw_dict[val] != pattern[idx]:
                    return False
            except KeyError:
                rw_dict[val] = pattern[idx]
        return True
