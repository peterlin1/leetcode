class Solution(object):

    def moveZeroes(self, nums):
        """
        Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of
        the non-zero elements.

        Note:

        You must do this in-place without making a copy of the array.
        Minimize the total number of operations.

        21 / 21 test cases passed.
        Status: Accepted
        Runtime: 52 ms
        Memory Usage: 14.9 MB


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

        l_idx = 0
        l_n = len(nums)
        for idx in range(l_n):
            if nums[idx] is 0:
                l_idx = max(idx, l_idx)
                while l_idx < l_n:
                    if nums[l_idx] is not 0:
                        nums[idx] = nums[l_idx]
                        nums[l_idx] = 0
                        break
                    l_idx += 1
                if l_idx == l_n:
                    break


if __name__ == "__main__":
    nums = [0, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)
