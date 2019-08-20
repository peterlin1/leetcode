class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        Write a function to find the longest common prefix string amongst an array of strings.

        If there is no common prefix, return an empty string ""

        Runtime: 36 ms, faster than 90.66% of Python3 online submissions for Longest Common Prefix.
        Memory Usage: 13.8 MB, less than 6.67% of Python3 online submissions for Longest Common Prefix.


        Parameters
        ----------
        strs : list


        Returns
        -------
        ret : str


        Examples
        --------
        >>> Solution().longestCommonPrefix(["flower","flow","flight"])
        'fl'

        >>> Solution().longestCommonPrefix(["dog","racecar","car"])
        ''

        >>> Solution().longestCommonPrefix(["ca","a"])
        ''

        """

        if len(strs) == 0:
            return ''
        ret = min(strs, key=len)

        while len(ret) is not 0:
            if all(s.startswith(ret) for s in strs):
                return ret
            else:
                ret = ret[:-1]
        return ret
