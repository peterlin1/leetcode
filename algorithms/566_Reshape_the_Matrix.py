class Solution(object):

    def matrixReshape(self, nums, r, c):
        """
        In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with
        different size but keep its original data.

        You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the
        row number and column number of the wanted reshaped matrix, respectively.

        The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing
        order as they were.

        If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix;
        Otherwise, output the original matrix.

        Note:
        The height and width of the given matrix is in range [1, 100].
        The given r and c are all positive.

        Runtime: 108 ms, faster than 41.56% of Python3 online submissions for Reshape the Matrix.
        Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Reshape the Matrix.


        Parameters
        ----------
        nums : list

        r : int

        c : int


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().matrixReshape([[1, 2], [3, 4]], r=1, c=4)
        [[1,2,3,4]]

        >>> Solution().matrixReshape([[1, 2], [3, 4]], r=2, c=4)
        [[1, 2], [3, 4]]

        """

        if r * c != len(nums) * len(nums[0]):
            return nums

        ret = [[None for i in range(c)] for j in range(r)]
        cnt = 0

        for row in range(len(nums)):
            for col in range(len(nums[0])):
                # print(f"{nums[row][col]}: {row} {col} New: {(cnt // c)} {(cnt % c)}")
                ret[cnt // c][cnt % c] = nums[row][col]
                cnt += 1
        return ret
