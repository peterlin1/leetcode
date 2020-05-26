class Solution(object):

    def maxUncrossedLines(self, A, B):
        """
        We write the integers of A and B (in the order they are given) on two separate horizontal lines.

        Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

        A[i] == B[j];
        The line we draw does not intersect any other connecting (non-horizontal) line.
        Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one
        connecting line.

        Return the maximum number of connecting lines we can draw in this way.

        Note:
        1 <= A.length <= 500
        1 <= B.length <= 500
        1 <= A[i], B[i] <= 2000

        74 / 74 test cases passed.
        Status: Accepted
        Runtime: 192 ms
        Memory Usage: 14 MB


        Parameters
        ----------
        A : list

        B : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().maxUncrossedLines([1, 4, 2], [1, 2, 4])
        2

        >>> Solution().maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2])
        3

        >>> Solution().maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]
        2

        """

        if len(A) < len(B):
            return self.maxUncrossedLines(B, A)

        mem = [0] * (len(B) + 1)
        for idx in range(len(A)):
            k = 0
            for jdx in range(1, len(mem)):
                _jdx = mem[jdx]
                if A[idx] == B[jdx - 1]:
                    mem[jdx] = k + 1
                else:
                    mem[jdx] = max(mem[jdx - 1], mem[jdx])
                k = _jdx
        return mem[-1]
