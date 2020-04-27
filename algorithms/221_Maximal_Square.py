class Solution(object):

    def maximalSquare(self, matrix):
        """
        Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its
        area.

        Runtime: 192 ms, faster than 90.38% of Python3 online submissions for Maximal Square.
        Memory Usage: 14.6 MB, less than 9.09% of Python3 online submissions for Maximal Square.


        Parameters
        ----------
        matrix : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().maximalSquare([[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]])
        4

        """

        if len(matrix) == 0:
            return 0

        mem = [0] * (len(matrix[0]) + 1)
        prev = ret = 0
        for idx in range(1, len(matrix) + 1):
            for jdx in range(1, len(matrix[0]) + 1):
                k = mem[jdx]
                if matrix[idx - 1][jdx - 1] == '1':
                    mem[jdx] = min(mem[jdx - 1], mem[jdx], prev) + 1
                else:
                    mem[jdx] = 0

                ret = max(mem[jdx], ret)
                prev = k

        return ret ** 2
