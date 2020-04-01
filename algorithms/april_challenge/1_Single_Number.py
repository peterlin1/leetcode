import functools


class Solution(object):

    def singleNumber(self, nums):
        """
        Given a non-empty array of integers, every element appears twice except for one. Find that single one.

        Note:
        Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

        16 / 16 test cases passed.
        Status: Accepted
        Runtime: 80 ms
        Memory Usage: 16.4 MB


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().singleNumber([2, 2, 1])
        1

        >>> Solution().singleNumber([4, 1, 2, 1, 2])
        4

        """

        return functools.reduce(lambda val1, val2: val1 ^ val2, nums)

