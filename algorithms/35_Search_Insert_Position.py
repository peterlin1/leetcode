class Solution(object):

    def searchInsert(self, nums, target):
        """
        Given a sorted array and a target value, return the index if the target is found. If not, return the index where
        it would be if it were inserted in order.

        You may assume no duplicates in the array.

        Runtime: 60 ms, faster than 60.93% of Python3 online submissions for Search Insert Position.
        Memory Usage: 14.4 MB, less than 5.97% of Python3 online submissions for Search Insert Position.


        Parameters
        ----------
        nums : list
        target : int

        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().searchInsert([1,3,5,6], 5)
        2

        >>> Solution().searchInsert([1,3,5,6], 2)
        1

        >>> Solution().searchInsert([1,3,5,6], 0)
        0

        >>> Solution().searchInsert([1,3,5,6], 7)
        4

        """

        for idx, val in enumerate(nums):
            if val >= target:
                return idx
        return len(nums)
