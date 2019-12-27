class Solution(object):

    def thirdMax(self, nums):
        """
        Given a non-empty array of integers, return the third maximum number in this array. If it does not exist,
        return the maximum number. The time complexity must be in O(n).

        Runtime: 56 ms, faster than 67.52% of Python3 online submissions for Third Maximum Number.
        Memory Usage: 13.6 MB, less than 92.31% of Python3 online submissions for Third Maximum Number.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().thirdMax([3, 2, 1])
        1

        >>> Solution().thirdMax([1, 2])
        2

        >>> Solution().thirdMax([2, 2, 3, 1])
        1

        """

        mem = [None] * 3
        for val in nums:
            if (mem[0] is None) or (val > mem[0]):
                mem[2] = mem[1]
                mem[1] = mem[0]
                mem[0] = val
            elif (mem[1] is None) or (val > mem[1]):
                if val != mem[0]:
                    mem[2] = mem[1]
                    mem[1] = val
            elif (mem[2] is None) or (val > mem[2]):
                if val != mem[1]:
                    mem[2] = val

        if mem[2] is not None:
            return mem[2]
        else:
            return mem[0]
