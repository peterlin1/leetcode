class Solution(object):

    def strStr(self, haystack, needle):
        """
        Implement strStr().

        Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

        Runtime: 32 ms, faster than 94.10% of Python3 online submissions for Implement strStr().
        Memory Usage: 14 MB, less than 12.31% of Python3 online submissions for Implement strStr().


        Parameters
        ----------
        haystack : str

        needle : str


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().strStr("hello", "ll")
        2

        >>> Solution().strStr("aaaaa", "bba")
        -1

        >>> Solution().strStr("mississippi", "issipi")
        -1

        """

        if len(needle) is 0:
            return 0
        for idx, ch in enumerate(haystack):
            if len(needle) > len(haystack) - idx:
                return -1
            pointer = 0
            while pointer < len(needle):
                if haystack[idx + pointer] == needle[pointer]:
                    pointer += 1
                else:
                    break
            if pointer == len(needle):
                return idx
        return -1
