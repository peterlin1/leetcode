class Solution(object):

    def countSquares(self, matrix):
        """
        Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

        Runtime: 904 ms, faster than 19.08% of Python3 online submissions for Count Square Submatrices with All Ones.
        Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Count Square Submatrices with All Ones.


        Parameters
        ----------
        matrix : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().countSquares([[0, 1, 1, 1],
        ...                          [1, 1, 1, 1],
        ...                          [0, 1, 1, 1]])
        15

        """

        if not matrix:
            return 0

        ret = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    if (col == 0) or (row == 0):
                        ret += 1
                    else:
                        n_ret = min(matrix[row - 1][col], matrix[row - 1][col - 1], matrix[row][col - 1]) + 1
                        ret += n_ret
                        matrix[row][col] = n_ret
        return ret
