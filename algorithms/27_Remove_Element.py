class Solution(object):
    def removeElement(self, nums, val):
        """
        Given an array nums and a value val, remove all instances of that value in-place and return the new length.

        Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
        extra memory.

        The order of elements can be changed. It doesn't matter what you leave beyond the new length.

        Runtime: 36 ms, faster than 90.94% of Python3 online submissions for Remove Element.
        Memory Usage: 13.7 MB, less than 6.06% of Python3 online submissions for Remove Element.



        Parameters
        ----------
        nums : list

        val : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().removeElement([3,2,2,3], 3)
        2

        """

        mem = 0
        if len(nums) is 0:
            return mem
        for num_val in nums:
            if num_val != val:
                nums[mem] = num_val
                mem += 1
        return mem
