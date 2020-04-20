class Solution(object):

    def search(self, nums, target):
        """
        Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

        (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

        You are given a target value to search. If found in the array return its index, otherwise return -1.

        You may assume no duplicate exists in the array.

        Your algorithm's runtime complexity must be in the order of O(log n).

        196 / 196 test cases passed.
        Status: Accepted
        Runtime: 44 ms
        Memory Usage: 14.1 MB


        Parameters
        ----------
        nums : list

        target : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
        4

        >>> Solution().search([4, 5, 6, 7, 0, 1, 2], 3)
        -1

        """

        # Find pivot point
        def _pivot_index(first, last):
            if last < first:
                return -1

            mid = int((first + last) / 2)

            if (mid < last) and (nums[mid] > nums[mid + 1]):
                return mid
            if (mid > first) and (nums[mid] < nums[mid - 1]):
                return mid - 1
            if nums[first] >= nums[mid]:
                return _pivot_index(first, mid - 1)
            return _pivot_index(mid + 1, last)

        def _search(first, last):
            if last < first:
                return -1
            mid = int((first + last) / 2)

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return _search(mid + 1, last)
            return _search(first, mid - 1)

        ret = _pivot_index(0, len(nums) - 1)
        if ret == -1:
            return _search(0, len(nums) - 1)
        if nums[ret] == target:
            return ret
        if nums[0] <= target:
            return _search(0, ret - 1)
        return _search(ret + 1, len(nums) - 1)
