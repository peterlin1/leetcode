class Solution(object):

    def solve(self, board):
        """
        Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

        A region is captured by flipping all 'O's into 'X's in that surrounded region.

        Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not
        flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

        59 / 59 test cases passed.
        Status: Accepted
        Runtime: 140 ms
        Memory Usage: 15.5 MB


        Parameters
        ----------
        board : list


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().solve([["X", "X", "X", "X"],
        ...                   ["X", "O", "O", "X"],
        ...                   ["X", "X", "O", "X"],
        ...                   ["X", "O", "X", "X"]])
        [["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"]]

        """

        if board == [] or board == [[]]:
            return

        n_rows = len(board)
        n_cols = len(board[0])

        _island_map = [[False for _x in range(n_cols)] for _y in range(n_rows)]

        def _mark(_row, _col):
            if (-1 < _row < n_rows) and (-1 < _col < n_cols) and (not _island_map[_row][_col]):
                _island_map[_row][_col] = True
                if board[_row][_col] == "O":
                    _mark(_row + 1, _col)
                    _mark(_row - 1, _col)
                    _mark(_row, _col + 1)
                    _mark(_row, _col - 1)

        for row in range(n_rows):
            if board[row][0] == "O":
                _mark(row, 0)
            if board[row][n_cols - 1] == "O":
                _mark(row, n_cols - 1)

        for col in range(n_cols):
            if board[0][col] == "O":
                _mark(0, col)
            if board[n_rows - 1][col] == "O":
                _mark(n_rows - 1, col)

        for row in range(1, n_rows - 1):
            for col in range(1, n_cols - 1):
                if not _island_map[row][col]:
                    board[row][col] = "X"
