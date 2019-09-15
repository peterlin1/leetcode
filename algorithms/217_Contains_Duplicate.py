class Solution(object):

    def containsDuplicate(self, nums):
        """
        Given an array of integers, find if the array contains any duplicates.

        Your function should return true if any value appears at least twice in the array, and it should return false
        if every element is distinct.

        Runtime: 120 ms, faster than 99.98% of Python3 online submissions for Contains Duplicate.
        Memory Usage: 19.2 MB, less than 16.98% of Python3 online submissions for Contains Duplicate.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().containsDuplicate([1, 2, 3, 1])
        True

        >>> Solution().containsDuplicate([1, 2, 3, 4])
        False

        """

        if len(nums) != len(set(nums)):
            return True
        return False
