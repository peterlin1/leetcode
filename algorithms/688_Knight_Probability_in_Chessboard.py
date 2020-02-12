class Solution(object):
    moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

    def knightProbability(self, N, K, r, c):
        """
        On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The
        rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

        A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal
        direction, then one square in an orthogonal direction.

        Taken almost entirely from accepted DP solution
        Runtime: 128 ms, faster than 97.37% of Python3 online submissions for Knight Probability in Chessboard.
        Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Knight Probability in Chessboard.


        Parameters
        ----------
        N : int
            Board size.

        K : int
            Number of moves.

        r : int
            Starting row index.

        c : int
            Starting column index.


        Returns
        -------
        ret : float

        """

        dp = [[0] * N for _ in range(N)]

        # step 0
        dp[r][c] = 1

        for _ in range(K):
            dp2 = [[0] * N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    if val is 0:
                        continue
                    for dr, dc in self.moves:
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            dp2[r + dr][c + dc] += val
            dp = dp2

        return sum(map(sum, dp)) / 8 ** K
