class Solution(object):
    def minMoves(self, nums):
        """
        Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements
        equal, where a move is incrementing n - 1 elements by 1.

        Runtime: 280 ms, faster than 41.63% of Python3 online submissions for Minimum Moves to Equal Array Elements.
        Memory Usage: 14 MB, less than 75.00% of Python3 online submissions for Minimum Moves to Equal Array Elements.


        Parameters
        ----------
        nums


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().minMoves([1, 2, 3])
        3

        """

        # ret = 0
        # minimum = min(nums)
        # for idx in range(len(nums)):
        #     ret += nums[idx] - minimum
        # return ret

        return sum(nums) - len(nums) * min(nums)


if __name__ == "__main__":
    print(Solution().minMoves([9, 1, 2, 3]))
