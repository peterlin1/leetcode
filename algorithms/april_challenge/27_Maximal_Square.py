class Solution(object):

    def maximalSquare(self, matrix):
        """
        Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its
        area.

        69 / 69 test cases passed.
        Status: Accepted
        Runtime: 204 ms
        Memory Usage: 14.6 MB


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

        ret = 0
        if len(matrix) == 0:
            return ret

        mem = [[0 for _x in range(len(matrix[0]) + 1)] for _y in range(len(matrix) + 1)]
        for idx in range(1, len(matrix) + 1):
            for jdx in range(1, len(matrix[0]) + 1):
                if matrix[idx - 1][jdx - 1] == '1':
                    mem[idx][jdx] = min(mem[idx][jdx - 1], mem[idx - 1][jdx - 1], mem[idx - 1][jdx]) + 1
                    ret = max(mem[idx][jdx], ret)
        return ret ** 2
