from collections import defaultdict


class Solution(object):

    def groupAnagrams(self, strs):
        """
        Given an array of strings, group anagrams together.

        Note:
        All inputs will be in lowercase.
        The order of your output does not matter.

        101 / 101 test cases passed.
        Status: Accepted
        Runtime: 152 ms
        Memory Usage: 16.5 MB


        Parameters
        ----------
        strs : list


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        [["ate","eat","tea"], ["nat","tan"], ["bat"]]

        """

        ret = defaultdict(list)

        for s_idx, s_word in enumerate(strs):
            ret["".join(sorted(s_word))].append(strs[s_idx])

        return list(ret.values())
