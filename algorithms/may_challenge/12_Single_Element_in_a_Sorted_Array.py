class Solution(object):

    def singleNonDuplicate(self, nums):
        """
        You are given a sorted array consisting of only integers where every element appears exactly twice, except for
        one element which appears exactly once. Find this single element that appears only once.

        Note: Your solution should run in O(log n) time and O(1) space.

        12 / 12 test cases passed.
        Status: Accepted
        Runtime: 76 ms
        Memory Usage: 15.9 MB


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])
        2

        >>> Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11])
        10

        """

        ret = 0
        for val in nums:
            if ret != 0 and ret != val:
                return ret
            ret ^= val
        return ret
