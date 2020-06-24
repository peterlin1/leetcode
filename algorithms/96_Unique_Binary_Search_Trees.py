from math import factorial


class Solution(object):

    def numTrees(self, n):
        """
        Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?


        Catalan number solution
        Runtime: 24 ms, faster than 92.98% of Python3 online submissions for Unique Binary Search Trees.
        Memory Usage: 13.7 MB, less than 91.26% of Python3 online submissions for Unique Binary Search Trees.


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
