class Solution(object):

    def rotate(self, matrix):
        """
        You are given an n x n 2D matrix representing an image.

        Rotate the image by 90 degrees (clockwise).

        Note:

        You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT
        allocate another 2D matrix and do the rotation.

        Runtime: 32 ms, faster than 74.02% of Python3 online submissions for Rotate Image.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Rotate Image.


        Parameters
        ----------
        matrix

        Returns
        -------
        ret : list

        """

        for row in range(len(matrix) // 2):
            matrix[row], matrix[len(matrix) - row - 1] = matrix[len(matrix) - row - 1], matrix[row]

        for row in range(len(matrix)):
            for col in range(row + 1, len(matrix[0])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]


if __name__ == "__main__":
    m = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    Solution().rotate(m)
    print(m)
