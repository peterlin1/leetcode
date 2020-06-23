class Solution(object):

    def singleNumber(self, nums):
        """
        Given a non-empty array of integers, every element appears three times except for one, which appears exactly
        once. Find that single one.

        Note:
        Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

        11 / 11 test cases passed.
        Status: Accepted
        Runtime: 56 ms
        Memory Usage: 15.2 MB


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
