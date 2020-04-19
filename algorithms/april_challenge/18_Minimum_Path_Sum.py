class Solution(object):

    def minPathSum(self, grid):
        """
        Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes
        the sum of all numbers along its path.

        Note: You can only move either down or right at any point in time.

        61 / 61 test cases passed.
        Status: Accepted
        Runtime: 136 ms
        Memory Usage: 15.3 MB


        Parameters
        ----------
        grid : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
        7

        """

        l_r = len(grid)
        l_c = len(grid[0])
        dp = [[0 for _x in range(l_c)] for _y in range(l_r)]

        # step 0
        dp[0][0] = grid[0][0]

        for r in range(1, l_r):
            dp[r][0] = dp[r - 1][0] + grid[r][0]

        for c in range(1, l_c):
            dp[0][c] = dp[0][c - 1] + grid[0][c]

        for r in range(1, l_r):
            for c in range(1, l_c):
                dp[r][c] = min(dp[r][c - 1], dp[r - 1][c]) + grid[r][c]

        return dp[-1][-1]
