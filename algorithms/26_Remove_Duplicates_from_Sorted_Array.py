class Solution(object):

    def removeDuplicates(self, nums):
        """
        Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the
        new length.

        Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
        extra memory.

        Runtime: 88 ms, faster than 97.87% of Python3 online submissions for Remove Duplicates from Sorted Array.
        Memory Usage: 15.5 MB, less than 5.74% of Python3 online submissions for Remove Duplicates from Sorted Array.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().removeDuplicates([1,1,2])
        2

        >>> Solution().removeDuplicates([])
        0

        """

        mem = 0
        if len(nums) is 0:
            return mem
        for val in nums:
            if val != nums[mem]:
                mem += 1
                nums[mem] = val
        return mem + 1
