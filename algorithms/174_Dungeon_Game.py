class Solution(object):

    def calculateMinimumHP(self, dungeon):
        """
        The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon
        consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left
        room and must fight his way through the dungeon to rescue the princess.

        The knight has an initial health point represented by a positive integer. If at any point his health point drops
        to 0 or below, he dies immediately.

        Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these
        rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

        In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in
        each step.

        Note:
        The knight's health has no upper bound.
        Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where
        the princess is imprisoned.

        Runtime: 60 ms, faster than 99.37% of Python3 online submissions for Dungeon Game.
        Memory Usage: 14.9 MB, less than 30.50% of Python3 online submissions for Dungeon Game.


        Parameters
        ----------
        dungeon : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().calculateMinimumHP([[-2, -3, 3], [-5, -10, 1] ,[ 10, 30, -5]])
        7

        """

        l_r = len(dungeon) - 1
        l_c = len(dungeon[0]) - 1

        for r in range(l_r, -1, -1):
            for c in range(l_c, -1, -1):
                if (r == l_r) and (c == l_c):
                    dungeon[r][c] = max(1, 1 - dungeon[r][c])
                elif r == l_r:
                    dungeon[r][c] = max(1, dungeon[r][c + 1] - dungeon[r][c])
                elif c == l_c:
                    dungeon[r][c] = max(1, dungeon[r + 1][c] - dungeon[r][c])
                else:
                    dungeon[r][c] = max(1, min(dungeon[r + 1][c], dungeon[r][c + 1]) - dungeon[r][c])

        # print(dungeon)
        return dungeon[0][0]
