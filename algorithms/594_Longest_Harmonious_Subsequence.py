class Solution(object):

    def findLHS(self, nums):
        """
        We define a harmounious array as an array where the difference between its maximum value and its minimum value
        is exactly 1.

        Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its
        possible subsequences.

        Note: The length of the input array will not exceed 20,000.

        Runtime: 412 ms, faster than 13.04% of Python3 online submissions for Longest Harmonious Subsequence.
        Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Longest Harmonious Subsequence.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().findLHS([1, 3, 2, 2, 5, 2, 3, 7])
        5

        """

        mem = {}
        ret = 0

        for val in nums:
            if val in mem:
                cnt = mem[val] + 1
                mem[val] += 1
            else:
                cnt = 1
                mem[val] = 1

            if (val - 1) in mem:
                ret = max(ret,
                          cnt + mem[val - 1])
            if (val + 1) in mem:
                ret = max(ret,
                          cnt + mem[val + 1])

        return ret
