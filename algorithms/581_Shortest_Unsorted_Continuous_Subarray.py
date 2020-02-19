class Solution(object):

    def findUnsortedSubarray(self, nums):
        """
        Given an integer array, you need to find one continuous subarray that if you only sort this subarray in
        ascending order, then the whole array will be sorted in ascending order, too.

        You need to find the shortest such subarray and output its length.

        Note:
        Then length of the input array is in range [1, 10,000].
        The input array may contain duplicates, so ascending order here means <=.

        Runtime: 200 ms, faster than 98.22% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
        Memory Usage: 13.9 MB, less than 90.00% of Python3 online submissions for Shortest Unsorted Continuous Subarray.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
        5

        """

        s_idx = 0
        e_idx = len(nums) - 1

        for idx in range(1, len(nums)):
            if nums[idx] < nums[idx - 1]:
                break
            s_idx = idx
        if s_idx == e_idx:
            return 0

        for idx in range(len(nums) - 2, -1, -1):
            if nums[idx] > nums[idx + 1]:
                break
            e_idx = idx

        e_val = max(nums[s_idx:e_idx + 1])
        s_val = min(nums[s_idx:e_idx + 1])
        while s_idx != 0:
            if nums[s_idx - 1] <= s_val:
                break
            s_idx -= 1

        while e_idx != len(nums) - 1:
            if nums[e_idx + 1] >= e_val:
                break
            e_idx += 1

        return e_idx - s_idx + 1
