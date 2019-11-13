# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):

    pass


class Solution(object):

    def firstBadVersion(self, n):
        """
        You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest
        version of your product fails the quality check. Since each version is developed based on the previous version,
        all the versions after a bad version are also bad.

        Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the
        following ones to be bad.

        You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function
        to find the first bad version. You should minimize the number of calls to the API.


        Modified binary search solution
        Runtime: 28 ms, faster than 94.38% of Python3 online submissions for First Bad Version.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for First Bad Version.


        Parameters
        ----------
        n : int


        Returns
        -------
        ret : int

        """

        def bin_search(left_edge, right_edge):
            if right_edge >= left_edge:
                mid = left_edge + (right_edge - left_edge) // 2
                ck = isBadVersion(mid)
                if ck:
                    return bin_search(left_edge, mid - 1)
                else:
                    return bin_search(mid + 1, right_edge)
            return left_edge

        return bin_search(1, n)
