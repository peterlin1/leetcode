class Solution(object):

    def findDuplicate(self, nums):
        """
        Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at
        least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

        Note:
        You must not modify the array (assume the array is read only).
        You must use only constant, O(1) extra space.
        Your runtime complexity should be less than O(n2).
        There is only one duplicate number in the array, but it could be repeated more than once.

        Runtime: 100 ms, faster than 19.00% of Python3 online submissions for Find the Duplicate Number.
        Memory Usage: 16.4 MB, less than 34.30% of Python3 online submissions for Find the Duplicate Number.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().findDuplicate([1, 3, 4, 2, 2])
        2

        >>> Solution().findDuplicate([3, 1, 3, 4, 2])
        3

        """

        if len(nums) < 2:
            return -1

        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow
