class Solution(object):

    def numIslands(self, grid):
        """
        Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by
        water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of
        the grid are all surrounded by water.

        47 / 47 test cases passed.
        Status: Accepted
        Runtime: 156 ms
        Memory Usage: 15 MB


        Parameters
        ----------
        grid : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().numIslands([[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]])
        1

        >>> Solution().numIslands([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]])
        3

        """

        _island_map = [[-1 if grid[_y][_x] == "1" else 0 for _x in range(len(grid[0]))] for _y in range(len(grid))]
        self.ret = 0

        def _mark(_row, _col):
            if (-1 < _row < len(grid)) and (-1 < _col < len(grid[0])) and (_island_map[_row][_col] is -1):
                if grid[_row][_col] == "1":
                    _island_map[_row][_col] = self.ret
                    _mark(_row + 1, _col)
                    _mark(_row - 1, _col)
                    _mark(_row, _col + 1)
                    _mark(_row, _col - 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if _island_map[row][col] > -1:
                    continue
                self.ret += 1
                _mark(row, col)

        return self.ret
