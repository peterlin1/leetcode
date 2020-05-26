class Solution(object):

    def findMaxLength(self, nums):
        """
        Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

        Note: The length of the given binary array will not exceed 50,000.

        555 / 555 test cases passed.
        Status: Accepted
        Runtime: 884 ms
        Memory Usage: 18.4 MB


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
