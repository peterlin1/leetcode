# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    pass


class Solution(object):

    def guessNumber(self, n):
        """
        We are playing the Guess Game. The game is as follows:

        I pick a number from 1 to n. You have to guess which number I picked.

        Every time you guess wrong, I'll tell you whether the number is higher or lower.

        You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

        -1 : My number is lower
         1 : My number is higher
         0 : Congrats! You got it!

        Runtime: 12 ms, faster than 88.02% of Python online submissions for Guess Number Higher or Lower.
        Memory Usage: 11.8 MB, less than 40.74% of Python online submissions for Guess Number Higher or Lower.


        Parameters
        ----------
        n : int


        Returns
        -------
        ret : int

        """

        def bin_search(left_edge, right_edge):
            if right_edge >= left_edge:
                mid = left_edge + (right_edge - left_edge) // 2
                ck = guess(mid)
                if ck == -1:
                    return bin_search(left_edge, mid - 1)
                if ck == 1:
                    return bin_search(mid + 1, right_edge)
                return mid

            return left_edge

        return bin_search(1, n)
