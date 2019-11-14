class Solution(object):
    def canWinNim(self, n):
        """
        You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one
        of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take
        the first turn to remove the stones.

        Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you
        can win the game given the number of stones in the heap.

        Runtime: 28 ms, faster than 95.83% of Python3 online submissions for Nim Game.
        Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Nim Game.


        Parameters
        ----------
        n : int


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().canWinNim(4)
        False

        """

        if n % 4 is 0:
            return False
        return True
