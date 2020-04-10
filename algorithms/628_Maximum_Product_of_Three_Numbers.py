class Solution(object):

    def maximumProduct(self, nums):
        """
        Given an integer array, find three numbers whose product is maximum and output the maximum product.

        Runtime: 276 ms, faster than 70.29% of Python3 online submissions for Maximum Product of Three Numbers.
        Memory Usage: 14.9 MB, less than 6.67% of Python3 online submissions for Maximum Product of Three Numbers.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : int

        """

        s_nums = sorted(nums)
        return max(s_nums[0] * s_nums[1] * s_nums[-1], s_nums[-1] * s_nums[-2] * s_nums[-3])
