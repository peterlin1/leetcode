class Solution(object):

    def arrayPairSum(self, nums):
        """
        Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1),
        (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

        Note:
        n is a positive integer, which is in the range of [1, 10000].
        All the integers in the array will be in the range of [-10000, 10000].

        Runtime: 284 ms, faster than 85.45% of Python3 online submissions for Array Partition I.
        Memory Usage: 15.2 MB, less than 6.06% of Python3 online submissions for Array Partition I.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().arrayPairSum([1, 4, 3, 2])
        4

        """

        sorted_a = sorted(nums)
        return sum([sorted_a[idx] for idx in range(0, len(sorted_a), 2)])
