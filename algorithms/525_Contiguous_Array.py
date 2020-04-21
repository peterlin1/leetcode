class Solution(object):

    def findMaxLength(self, nums):
        """
        Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

        Note: The length of the given binary array will not exceed 50,000.

        Runtime: 900 ms, faster than 74.97% of Python3 online submissions for Contiguous Array.
        Memory Usage: 18.1 MB, less than 16.67% of Python3 online submissions for Contiguous Array.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().findMaxLength([0, 1])
        2

        >>> Solution().findMaxLength([0, 0, 0, 0, 1, 0, 1, 1, 1])
        8

        """

        mem = {}
        c_sum = 0
        ret = 0
        for idx in range(len(nums)):
            if nums[idx] is 0:
                c_sum -= 1
            else:
                c_sum += 1

            if c_sum is 0:
                ret = idx + 1
                continue

            try:
                ret = max(ret, idx - mem[c_sum])
            except KeyError:
                mem[c_sum] = idx

        return ret
