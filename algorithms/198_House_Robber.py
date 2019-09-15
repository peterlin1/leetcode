class Solution(object):

    def rob(self, nums):
        """
        You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
        stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system
        connected and it will automatically contact the police if two adjacent houses were broken into on the same
        night.

        Given a list of non-negative integers representing the amount of money of each house, determine the maximum
        amount of money you can rob tonight without alerting the police.

        Runtime: 40 ms, faster than 48.83% of Python3 online submissions for House Robber.
        Memory Usage: 13.9 MB, less than 9.09% of Python3 online submissions for House Robber.


        Parameters
        ----------
        nums : list

        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().rob([1, 2, 3, 1])
        4

        >>> Solution().rob([2, 7, 9, 3, 1])
        12

        >>> Solution().rob([2, 1, 1, 2])
        4

        """

        # DP forward solution
        mem_r = [0] * len(nums)
        try:
            mem_r[0] = nums[0]
        except IndexError:
            return 0
        try:
            mem_r[1] = max(nums[0], nums[1])
        except IndexError:
            return mem_r[0]
        for idx in range(2, len(nums)):
            mem_r[idx] = max(mem_r[idx - 1], nums[idx] + mem_r[idx - 2])
        return mem_r[-1]
