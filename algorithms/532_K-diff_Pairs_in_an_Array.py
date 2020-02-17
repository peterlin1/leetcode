class Solution(object):

    def findPairs(self, nums, k):
        """
        Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array.
        Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their
        absolute difference is k.

        Note:
        The pairs (i, j) and (j, i) count as the same pair.
        The length of the array won't exceed 10,000.
        All the integers in the given input belong to the range: [-1e7, 1e7].

        Runtime: 132 ms, faster than 65.30% of Python3 online submissions for K-diff Pairs in an Array.
        Memory Usage: 14 MB, less than 96.77% of Python3 online submissions for K-diff Pairs in an Array.


        Parameters
        ----------
        nums : list

        k : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().findPairs([3, 1, 4, 1, 5], 2)
        2

        >>> Solution().findPairs([1, 2, 3, 4, 5], 1)
        4

        >>> Solution().findPairs([1, 3, 1, 5, 4], 0)
        1

        """
        if k < 0:
            return 0

        mem = {}
        ret = 0
        for val in nums:
            if val not in mem:
                if val - k in mem:
                    ret += 1
                if val + k in mem:
                    ret += 1
            elif k == 0:
                if mem[val] is 1:
                    ret += 1
            try:
                mem[val] += 1
            except KeyError:
                mem[val] = 1

        return ret
