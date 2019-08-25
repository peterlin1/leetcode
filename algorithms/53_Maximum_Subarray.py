class Solution(object):

    def maxSubArray(self, nums):
        """
        Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
        sum and return its sum.

        Runtime: 76 ms, faster than 76.69% of Python3 online submissions for Maximum Subarray.
        Memory Usage: 14.8 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6

        """

        mem = [0] * len(nums)
        for idx, val in enumerate(nums):
            try:
                mem[idx] = max(val, val + mem[idx - 1])
            except IndexError:
                mem[idx] = nums[idx]
            # print(mem)
        return max(mem)

