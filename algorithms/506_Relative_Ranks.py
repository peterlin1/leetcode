class Solution(object):

    def findRelativeRanks(self, nums):
        """
        Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will
        be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

        Note:
        N is a positive integer and won't exceed 10,000.
        All the scores of athletes are guaranteed to be unique.

        Runtime: 6304 ms, faster than 5.12% of Python3 online submissions for Relative Ranks.
        Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Relative Ranks.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().findRelativeRanks([5, 4, 3, 2, 1])
        ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

        """

        ret = [0] * len(nums)

        for idx in range(len(nums)):
            for jdx in range(idx + 1, len(nums)):
                if nums[jdx] > nums[idx]:
                    ret[idx] += 1

            for jdx in range(idx - 1, -1, -1):
                if nums[jdx] > nums[idx]:
                    ret[idx] += 1
            if ret[idx] is 0:
                ret[idx] = 'Gold Medal'
            elif ret[idx] is 1:
                ret[idx] = 'Silver Medal'
            elif ret[idx] is 2:
                ret[idx] = 'Bronze Medal'
            else:
                ret[idx] = str(ret[idx] + 1)
        return ret
