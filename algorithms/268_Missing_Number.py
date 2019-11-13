class Solution(object):
    def missingNumber(self, nums):
        """
        Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the
        array.

        Runtime: 144 ms, faster than 95.04% of Python3 online submissions for Missing Number.
        Memory Usage: 14.1 MB, less than 70.97% of Python3 online submissions for Missing Number.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().missingNumber([3, 0, 1])
        2

        >>> Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
        8

        """

        e_sum = 0
        n_sum = 0
        for idx in range(len(nums) + 1):
            e_sum += idx
            try:
                n_sum += nums[idx]
            except IndexError:
                pass
        return e_sum - n_sum

