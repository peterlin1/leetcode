class Solution(object):

    def intersect(self, nums1, nums2):
        """
        Given two arrays, write a function to compute their intersection.

        Each element in the result should appear as many times as it shows in both arrays.
        The result can be in any order.

        Runtime: 48 ms, faster than 89.20% of Python3 online submissions for Intersection of Two Arrays II.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Intersection of Two Arrays II.


        Parameters
        ----------
        nums1 : list

        nums2 : list


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().intersect([1, 2, 2, 1], [2, 2])
        [2, 2]

        >>> Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4])
        [4, 9]

        """

        ret = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i_n = 0
        for idx in range(len(nums1)):
            try:
                while nums2[i_n] < nums1[idx]:
                    i_n += 1
            except IndexError:
                return ret
            if nums1[idx] == nums2[i_n]:
                ret.append(nums1[idx])
                i_n += 1
        return ret
