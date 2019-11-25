class Solution(object):

    def intersection(self, nums1, nums2):
        """
        Given two arrays, write a function to compute their intersection.

        Note:
        - Each element in the result must be unique.
        - The result can be in any order.

        Runtime: 40 ms, faster than 98.31% of Python3 online submissions for Intersection of Two Arrays.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Intersection of Two Arrays.


        Parameters
        ----------
        nums1 : list

        nums2 : list


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().intersection([1, 2, 2, 1], [2, 2])
        [2]

        """

        return list(set(nums1) & set(nums2))
