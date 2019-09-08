class Solution(object):

    def majorityElement(self, nums):
        """
        Given an array of size n, find the majority element. The majority element is the element that appears more
        than ⌊ n/2 ⌋ times.

        You may assume that the array is non-empty and the majority element always exist in the array.

        Runtime: 196 ms, faster than 66.96% of Python3 online submissions for Majority Element.
        Memory Usage: 15.2 MB, less than 7.14% of Python3 online submissions for Majority Element.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().majorityElement([3, 2, 3])
        3

        >>> Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])
        2

        >>> Solution().majorityElement([0,0,0,0,0,0,0,0,0,0,0,0,1])
        0

        """

        mem = {}
        l = len(nums) // 2 + 1
        for val in nums:
            try:
                cnt = mem[val] + 1
                if cnt == l:
                    return val
                mem[val] = cnt
            except KeyError:
                mem[val] = 1
        return nums[0]
