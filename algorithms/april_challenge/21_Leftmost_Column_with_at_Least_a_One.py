# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """


class BinaryMatrix(object):

    def get(self, x, y):
        pass

    def dimensions(self):
        pass


class Solution(object):

    def leftMostColumnWithOne(self, binaryMatrix):
        """
        A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in
        non-decreasing order.

        Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it.
        If such index doesn't exist, return -1.

        You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

        BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
        BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
        Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions
        that attempt to circumvent the judge will result in disqualification.

        For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will
        not have access the binary matrix directly.

        Constraints:
        1 <= mat.length, mat[i].length <= 100
        mat[i][j] is either 0 or 1.
        mat[i] is sorted in a non-decreasing way.

        37 / 37 test cases passed.
        Status: Accepted
        Runtime: 100 ms
        Memory Usage: 14.1 MB


        Parameters
        ----------
        binaryMatrix : BinaryMatrix


        Returns
        -------
        ret : int

        """

        # rows, cols
        shape = binaryMatrix.dimensions()
        pointer = [0, shape[1] - 1]
        ret = -1

        while pointer[0] < shape[0] or pointer[1] > -1:
            if binaryMatrix.get(pointer[0], pointer[1]) is 1:
                ret = pointer[1]
                if pointer[1] == 0:
                    return ret
                pointer[1] -= 1
            else:
                if pointer[0] == (shape[0] - 1):
                    return ret
                pointer[0] += 1
        return ret
