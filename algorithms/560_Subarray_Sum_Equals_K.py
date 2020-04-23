from collections import Counter


class Solution(object):

    def subarraySum(self, nums, k):
        """
        Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum
        equals to k.

        Note:
        The length of the array is in range [1, 20,000].
        The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

        Runtime: 120 ms, faster than 43.55% of Python3 online submissions for Subarray Sum Equals K.
        Memory Usage: 16.3 MB, less than 20.00% of Python3 online submissions for Subarray Sum Equals K.


        Parameters
        ----------
        nums : list

        k : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().subarraySum([1, 1, 1], 2)
        2

        """

        mem = Counter()
        ret = 0
        c_sum = 0

        for val in nums:
            c_sum += val
            if c_sum == k:
                ret += 1

            if c_sum - k in mem:
                ret += mem[c_sum - k]

            mem[c_sum] += 1

        return ret
