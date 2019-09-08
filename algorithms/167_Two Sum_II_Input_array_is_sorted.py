class Solution(object):

    def twoSum(self, numbers, target):
        """
        Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

        The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

        Note:

        Your returned answers (both index1 and index2) are not zero-based.
        You may assume that each input would have exactly one solution and you may not use the same element twice.

        Runtime: 72 ms, faster than 84.40% of Python3 online submissions for Two Sum II - Input array is sorted.
        Memory Usage: 14 MB, less than 5.80% of Python3 online submissions for Two Sum II - Input array is sorted.


        Parameters
        ----------
        numbers : list

        target : int


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().twoSum([2, 7, 11, 15], 9)
        [1, 2]

        >>> Solution().twoSum([2, 7, 7, 15], 14)
        [2, 3]
        """

        mem = {}
        for idx in range(len(numbers)):
            try:
                return [mem[numbers[idx]] + 1, idx + 1]
            except KeyError:
                mem[target - numbers[idx]] = idx
        return []
