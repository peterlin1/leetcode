class Solution(object):

    def maxCount(self, m, n, ops):
        """
        Given an m * n matrix M initialized with all 0's and several update operations.

        Operations are represented by a 2D array, and each operation is represented by an array with two positive
        integers a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.

        You need to count and return the number of maximum integers in the matrix after performing all the operations.

        Note:
        The range of m and n is [1,40000].
        The range of a is [1,m], and the range of b is [1,n].
        The range of operations size won't exceed 10,000.

        Runtime: 72 ms, faster than 54.99% of Python3 online submissions for Range Addition II.
        Memory Usage: 14.8 MB, less than 33.33% of Python3 online submissions for Range Addition II.


        Parameters
        ----------
        m : int

        n : int

        ops : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().maxCount(3, 3, [[2, 2], [3, 3]])
        4

        """
        if not ops:
            return m * n

        t_a = list(map(min, zip(*ops)))
        return t_a[0] * t_a[1]
