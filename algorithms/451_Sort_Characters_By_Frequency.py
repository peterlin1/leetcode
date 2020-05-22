from collections import Counter


class Solution(object):

    def frequencySort(self, s):
        """
        Given a string, sort it in decreasing order based on the frequency of characters.

        Runtime: 56 ms, faster than 39.28% of Python3 online submissions for Sort Characters By Frequency.
        Memory Usage: 15 MB, less than 7.14% of Python3 online submissions for Sort Characters By Frequency.


        Parameters
        ----------
        s : str


        Returns
        -------
        ret : str


        Examples
        --------
        >>> Solution().frequencySort("tree")
        "eert"

        >>> Solution().frequencySort("cccaaa")
        "cccaaa"

        >>> Solution().frequencySort("Aabb")
        "bbAa"

        """

        c_s = Counter(s)
        l = [char[0] * char[1] for char in c_s.most_common()]
        return "".join(l)
