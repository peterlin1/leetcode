class Solution(object):
    def moveZeroes(self, nums):
        """
        Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of
        the non-zero elements.

        Note:

        You must do this in-place without making a copy of the array.
        Minimize the total number of operations.

        Runtime: 1656 ms, faster than 5.05% of Python3 online submissions for Move Zeroes.
        Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Move Zeroes.


        Parameters
        ----------
        nums : list


        Examples
        --------
        >>> nums = [0, 1, 0, 3, 12]
        >>> Solution().moveZeroes(nums)
        >>> print(nums)
        >>> [1, 3, 12, 0, 0]

        """

        def swap(m, n):
            tmp = nums[m]
            nums[m] = nums[n]
            nums[n] = tmp

        for idx in range(len(nums)):
            if nums[idx] is 0:
                l_idx = idx
                r_idx = idx + 1
                while r_idx != len(nums):
                    if nums[r_idx] != 0:
                        swap(l_idx, r_idx)
                        l_idx = r_idx
                    r_idx += 1


if __name__ == "__main__":
    nums = [0, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)
