from collections import defaultdict


class Solution(object):

    def groupAnagrams(self, strs):
        """
        Given an array of strings, group anagrams together.

        Note:
        All inputs will be in lowercase.
        The order of your output does not matter.

        Runtime: 100 ms, faster than 82.81% of Python3 online submissions for Group Anagrams.
        Memory Usage: 16.8 MB, less than 41.51% of Python3 online submissions for Group Anagrams.


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

        for s_word in strs:
            ret["".join(sorted(s_word))].append(s_word)

        return list(ret.values())
