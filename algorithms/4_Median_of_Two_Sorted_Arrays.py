class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        There are two sorted arrays nums1 and nums2 of size m and n respectively.

        Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

        You may assume nums1 and nums2 cannot be both empty.


        Parameters
        ----------
        nums1 : list
        nums2 : list


        Returns
        -------
        ret : float


        Examples
        --------
        >>> nums1 = [1, 3]
        >>> nums2 = [2]
        >>> Solution().findMedianSortedArrays(nums1, nums2)
        2.0

        """
        len1 = len(nums1)
        len2 = len(nums2)

        if len1 == 0:
            return (nums2[(len2-1) // 2] + nums2[round((len2-1) / 2)]) / 2
        elif len2 == 0:
            return (nums1[(len1-1) // 2] + nums1[round((len1-1) / 2)]) / 2

        if len2 < len1:
            return Solution().findMedianSortedArrays(nums2, nums1)

        target_offset = (len1 + len2) // 2



def binary_search(l1, target, ltd, rtd):
    mid_index = ltd + (rtd - ltd) // 2
    if l1[mid_index] == target:
        return mid_index
    elif l1[mid_index] > target:
        return binary_search(l1, target, ltd, mid_index-1)
    else:
        return binary_search(l1, target, mid_index+1, rtd)


if __name__ == "__main__":
    # print(binary_search([0, 1, 2, 3, 4, 10], 10, 0, 5))
    print(Solution().findMedianSortedArrays([0, 176, 287, 980], []))
