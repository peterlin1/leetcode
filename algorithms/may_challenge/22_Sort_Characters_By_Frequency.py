from collections import Counter


class Solution(object):

    def frequencySort(self, s):
        """
        Given a string, sort it in decreasing order based on the frequency of characters.

        35 / 35 test cases passed.
        Status: Accepted
        Runtime: 40 ms
        Memory Usage: 15.1 MB


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
