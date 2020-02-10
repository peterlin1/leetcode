class Solution(object):

    def findMaxConsecutiveOnes(self, nums):
        """
        Given a binary array, find the maximum number of consecutive 1s in this array.

        Note:

        The input array will only contain 0 and 1.
        The length of input array is a positive integer and will not exceed 10,000

        Runtime: 364 ms, faster than 93.71% of Python3 online submissions for Max Consecutive Ones.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Max Consecutive Ones.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
        3

        """

        max_one = 0
        curr = 0
        for bit in nums:
            if bit is 0:
                max_one = max(max_one, curr)
                curr = 0
            else:
                curr += 1
        max_one = max(max_one, curr)
        return max_one
