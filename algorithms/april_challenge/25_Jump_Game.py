class Solution(object):

    def canJump(self, nums):
        """
        Given an array of non-negative integers, you are initially positioned at the first index of the array.

        Each element in the array represents your maximum jump length at that position.

        Determine if you are able to reach the l_idx index.

        75 / 75 test cases passed.
        Status: Accepted
        Runtime: 84 ms
        Memory Usage: 15.9 MB


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().canJump([2, 3, 1, 1, 4])
        True

        >>> Solution().canJump([3, 2, 1, 0, 4])
        False

        """

        # l_idx = len(nums) - 1
        # for pos in range(l_idx - 1, -1, -1):
        #     if pos + nums[pos] >= l_idx:
        #         l_idx = pos
        # return l_idx <= 0

        l_idx = 0
        for pos in range(len(nums)):
            if l_idx < pos:
                return False
            if pos + nums[pos] > l_idx:
                l_idx = pos + nums[pos]
        return True
