class Solution(object):

    def minDistance(self, word1, word2):
        """
        Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

        You have the following 3 operations permitted on a word:
        Insert a character
        Delete a character
        Replace a character

        1146 / 1146 test cases passed.
        Status: Accepted
        Runtime: 184 ms
        Memory Usage: 17.3 MB


        Parameters
        ----------
        word1 : str

        word2 : str


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().minDistance("horse", "ros")
        3

        >>> Solution().minDistance("intention", "execution")
        5

        """

        table = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            table[i][0] = i
        for j in range(len(word2) + 1):
            table[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])

        # print(table)
        return table[-1][-1]
