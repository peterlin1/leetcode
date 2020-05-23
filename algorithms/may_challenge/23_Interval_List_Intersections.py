class Solution(object):

    def intervalIntersection(self, A, B):
        """
        Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

        Return the intersection of these two interval lists.

        (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The
        intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a
        closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

        Note:
        0 <= A.length < 1000
        0 <= B.length < 1000
        0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

        86 / 86 test cases passed.
        Status: Accepted
        Runtime: 192 ms
        Memory Usage: 14.6 MB


        Parameters
        ----------
        A : list

        B : list


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().intervalIntersection(A=[[0, 2], [5, 10], [13, 23], [24, 25]], B=[[1, 5], [8, 12], [15, 24], [25, 26]])
        [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

        """

        ret = []
        idx = jdx = 0
        while idx < len(A) and jdx < len(B):
            if A[idx][1] >= B[jdx][0] and B[jdx][1] >= A[idx][0]:
                ret.append([max(A[idx][0], B[jdx][0]), min(A[idx][1], B[jdx][1])])
            if A[idx][1] < B[jdx][1]:
                idx += 1
            else:
                jdx += 1
        return ret
