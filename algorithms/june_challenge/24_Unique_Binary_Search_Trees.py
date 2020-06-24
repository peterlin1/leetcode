from math import factorial


class Solution(object):

    def numTrees(self, n):
        """
        Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?


        Catalan number solution
        19 / 19 test cases passed.
        Status: Accepted
        Runtime: 32 ms
        Memory Usage: 13.9 MB


        Parameters
        ----------
        n : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().numTrees(3)
        5

        """

        return int(factorial(2 * n) / (factorial(n) * factorial(n + 1)))
