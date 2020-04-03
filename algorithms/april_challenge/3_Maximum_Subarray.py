class Solution(object):

    def maxSubArray(self, nums):
        """
        Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
        sum and return its sum.

        Follow up:
        If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
        which is more subtle.

        202 / 202 test cases passed.
        Status: Accepted
        Runtime: 52 ms
        Memory Usage: 14.7 MB


        Parameters
        ----------
        nums : list of int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6

        """

        # prev = ret = nums[0]
        # for val in nums[1:]:
        #     ret = max(ret, val, val + prev)
        #     prev = max(val, val + prev)
        # return ret

        mem = [0] * len(nums)
        for idx, val in enumerate(nums):
            try:
                mem[idx] = max(val, val + mem[idx - 1])
            except IndexError:
                mem[idx] = val
        return max(mem)
