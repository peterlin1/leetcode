class Solution(object):

    def findDisappearedNumbers(self, nums):
        """
        Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear
        once.

        Find all the elements of [1, n] inclusive that do not appear in this array.

        Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as
        extra space.

        Runtime: 376 ms, faster than 73.37% of Python3 online submissions for Find All Numbers Disappeared in an Array.
        Memory Usage: 22.9 MB, less than 7.14% of Python3 online submissions for Find All Numbers Disappeared in an Array.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
        [5, 6]

        """

        return list(set([val for val in range(1, len(nums) + 1)]) - set(nums))
