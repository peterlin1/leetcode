class Solution(object):

    def nextGreaterElement(self, nums1, nums2):
        """
        You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find
        all the next greater numbers for nums1's elements in the corresponding places of nums2.

        The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not
        exist, output -1 for this number.

        Note:
        All elements in nums1 and nums2 are unique.
        The length of both nums1 and nums2 would not exceed 1000.

        Runtime: 72 ms, faster than 32.93% of Python3 online submissions for Next Greater Element I.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Next Greater Element I.


        Parameters
        ----------
        nums1 : list

        nums2 : list


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
        [-1, 3, -1]

        """

        ret = [-1] * len(nums1)
        for idx_1 in range(len(nums1)):
            for idx in range(nums2.index(nums1[idx_1]), len(nums2)):
                if nums2[idx] > nums1[idx_1]:
                    ret[idx_1] = nums2[idx]
                    break
        return ret
