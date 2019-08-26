class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

        Runtime: 48 ms, faster than 35.56% of Python3 online submissions for Merge Sorted Array.
        Memory Usage: 14 MB, less than 6.15% of Python3 online submissions for Merge Sorted Array.


        Parameters
        ----------
        nums1 : list

        m : int

        nums2 : list

        n : int


        Examples
        --------
        >>> num1 = [1, 2, 3, 0, 0, 0]
        >>> Solution().merge(num1, 3, [2, 5, 6], 3)
        >>> print(num1)
        [1, 2, 2, 3, 5, 6]


        Notes
        -----
        The number of elements initialized in nums1 and nums2 are m and n respectively.
        You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements
        from nums2.

        """

        while n > 0:
            if (m == 0) or (nums2[n - 1] >= nums1[m - 1]):
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                nums1[m - 1] = 0
                m -= 1


if __name__ == "__main__":
    num1 = [1, 2, 3, 0, 0, 0, 0]
    Solution().merge(num1, 3, [1, 2, 5, 6], 4)
    print(num1)

    num1 = [2, 0]
    Solution().merge(num1, 1, [1], 1)
    print(num1)

    num1 = [0]
    Solution().merge(num1, 0, [1], 1)
    print(num1)

    num1 = [4, 5, 6, 0, 0, 0]
    Solution().merge(num1, 3, [1, 2, 3], 3)
    print(num1)
