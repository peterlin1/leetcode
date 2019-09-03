class Solution(object):

    def generate(self, numRows):
        """
        Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

        In Pascal's triangle, each number is the sum of the two numbers directly above it.

        Example:

        Input: 5
        Output:
        [
             [1],
            [1,1],
           [1,2,1],
          [1,3,3,1],
         [1,4,6,4,1]
        ]

        Runtime: 36 ms, faster than 75.23% of Python3 online submissions for Pascal's Triangle.
        Memory Usage: 13.7 MB, less than 7.14% of Python3 online submissions for Pascal's Triangle.


        Parameters
        ----------
        numRows : int


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().generate(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

        """
        ret = []
        for n in range(1, numRows + 1):
            _base = [1]
            for k in range(1, n):
                _base.append(int(_base[k - 1] * (n - k) / k))
            ret.append(_base)
        return ret
