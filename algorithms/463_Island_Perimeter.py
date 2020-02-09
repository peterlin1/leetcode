class Solution(object):

    def islandPerimeter(self, grid):
        """
        You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

        Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
        and there is exactly one island (i.e., one or more connected land cells).

        The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is
        a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter
        of the island.

        Runtime: 552 ms, faster than 59.49% of Python3 online submissions for Island Perimeter.
        Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Island Perimeter.


        Parameters
        ----------
        grid : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().islandPerimeter([[0, 1, 0, 0],
        ...                             [1, 1, 1, 0],
        ...                             [0, 1, 0, 0],
        ...                             [1, 1, 0, 0]])
        16

        """

        def _fencing(x_idx, y_idx):
            if x_idx is -1 or y_idx is -1:
                return 0
            try:
                return grid[x_idx][y_idx]
            except IndexError:
                return 0

        ret = 0
        for x_idx in range(len(grid)):
            for y_idx in range(len(grid[0])):
                if grid[x_idx][y_idx] is 1:
                    ret += 4 - _fencing(x_idx - 1, y_idx) - _fencing(x_idx + 1, y_idx) - _fencing(x_idx, y_idx - 1) - _fencing(x_idx, y_idx + 1)
        return ret
