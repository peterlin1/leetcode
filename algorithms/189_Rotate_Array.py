class Solution(object):

    def rotate(self, nums, k):
        """
        Given an array, rotate the array to the right by k steps, where k is non-negative.
        Do not return anything, modify nums in-place instead.

        Runtime: 76 ms, faster than 55.07% of Python3 online submissions for Rotate Array.
        Memory Usage: 15 MB, less than 5.09% of Python3 online submissions for Rotate Array.


        Parameters
        ----------
        nums
        k

        Examples
        --------
        >>> Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
        # [5, 6, 7, 1, 2, 3, 4]

        """
        mem = nums.copy()
        l_n = len(nums)
        for idx in range(l_n):
            nums[idx] = mem[idx - (k % l_n)]


if __name__ == "__main__":
    ex1 = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(ex1, 10)
    print(ex1)
