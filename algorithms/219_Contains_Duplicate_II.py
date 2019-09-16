class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        """
        Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the
        array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

        Runtime: 112 ms, faster than 48.24% of Python3 online submissions for Contains Duplicate II.
        Memory Usage: 21.4 MB, less than 43.75% of Python3 online submissions for Contains Duplicate II.


        Parameters
        ----------
        nums : list

        k : int


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().containsNearbyDuplicate([1, 0, 1, 1], 1)
        True

        >>> Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
        False

        """
        mem = {}
        for idx, val in enumerate(nums):
            if val not in mem:
                mem[val] = idx
            else:
                if (idx - mem[val]) <= k:
                    return True
                mem[val] = idx
        return False
