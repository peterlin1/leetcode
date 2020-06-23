class Solution(object):

    def singleNumber(self, nums):
        """
        Given a non-empty array of integers, every element appears three times except for one, which appears exactly
        once. Find that single one.

        Note:
        Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

        Runtime: 56 ms, faster than 83.79% of Python3 online submissions for Single Number II.
        Memory Usage: 15.4 MB, less than 74.31% of Python3 online submissions for Single Number II.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().singleNumber([2, 2, 3, 2])
        3

        >>> Solution().singleNumber([0, 1, 0, 1, 0, 1, 99])
        99

        """

        ones = twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones
