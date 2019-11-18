class NumArray(object):

    def __init__(self, nums):
        """
        Parameters
        ----------
        nums : list

        """

        self.sum_num = [0] * len(nums)
        t_sum = 0
        for idx in range(len(nums)):
            t_sum = t_sum + nums[idx]
            self.sum_num[idx] = t_sum

    def sumRange(self, i, j):
        """
        Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

        Runtime: 80 ms, faster than 96.22% of Python3 online submissions for Range Sum Query - Immutable.
        Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Range Sum Query - Immutable.


        Parameters
        ----------
        i : int

        j : int


        Returns
        -------
        ret : int

        """

        if i == 0:
            return self.sum_num[j]
        return self.sum_num[j] - self.sum_num[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    param_1 = obj.sumRange(2, 5)
    print(param_1)