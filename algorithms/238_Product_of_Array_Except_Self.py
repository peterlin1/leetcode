class Solution(object):

    def productExceptSelf(self, nums):
        """
        Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the
        product of all the elements of nums except nums[i].

        Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the
        whole array) fits in a 32 bit integer.

        Note: Please solve it without division and in O(n).

        Follow up:
        Could you solve it with constant space complexity? (The output array does not count as extra space for the
        purpose of space complexity analysis.)

        Runtime: 124 ms, faster than 66.33% of Python3 online submissions for Product of Array Except Self.
        Memory Usage: 20.9 MB, less than 8.00% of Python3 online submissions for Product of Array Except Self.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().productExceptSelf([1, 2, 3, 4])
        [24, 12, 8, 6]

        """

        # Guaranteed to be > 1
        # if len(nums) is 1:
        #     return [0]

        mem_f = [1] * len(nums)
        mem_b = [1] * len(nums)

        for idx in range(1, len(nums)):
            mem_f[idx] = nums[idx - 1] * mem_f[idx - 1]

        for idx in range(len(nums) - 2, -1, -1):
            mem_b[idx] = nums[idx + 1] * mem_b[idx + 1]

        return [mem_f[factor_i] * mem_b[factor_i] for factor_i in range(len(nums))]
