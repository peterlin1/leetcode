class Solution(object):

    def getRow(self, rowIndex):
        """
        Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

        Note that the row index starts from 0.

        Runtime: 36 ms, faster than 75.71% of Python3 online submissions for Pascal's Triangle II.
        Memory Usage: 13.7 MB, less than 7.69% of Python3 online submissions for Pascal's Triangle II.


        Parameters
        ----------
        rowIndex : int


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().getRow(3)
        [1,3,3,1]

        """

        ret = [1]
        for k in range(1, rowIndex + 1):
            ret.append(int(ret[k - 1] * (rowIndex + 1 - k) / k))
        return ret
