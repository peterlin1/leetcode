class Solution(object):

    def singleNumber(self, nums):
        """
        Given a non-empty array of integers, every element appears twice except for one. Find that single one.

        Note:

        Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

        Runtime: 100 ms, faster than 68.71% of Python3 online submissions for Single Number.
        Memory Usage: 15.8 MB, less than 6.56% of Python3 online submissions for Single Number.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().singleNumber([2, 2, 1])
        1

        >>> Solution().singleNumber([4, 1, 2, 1, 2])
        4

        >>> Solution().singleNumber([3, 3, 1, 2, 1, 2, 4])
        4

        """

        # Another neat method utilizing bit-wise XOR
        for idx in range(1, len(nums)):
            nums[idx] ^= nums[idx - 1]
        return nums[-1]

        # nums.sort()
        # for idx in range(0, len(nums) - 1, 2):
        #     if nums[idx] != nums[idx + 1]:
        #         return nums[idx]
        # return nums[-1]

