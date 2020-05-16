class Solution(object):

    def maxSubarraySumCircular(self, A):
        """
        Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of
        C.

        Here, a circular array means the end of the array connects to the beginning of the array.  (Formally,
        C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

        Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray
        C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

        109 / 109 test cases passed.
        Status: Accepted
        Runtime: 548 ms
        Memory Usage: 18.1 MB


        Parameters
        ----------
        A : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().maxSubarraySumCircular([1, -2, 3, -2])
        3

        >>> Solution().maxSubarraySumCircular([5, -3, 5])
        10

        >>> Solution().maxSubarraySumCircular([3, -1, 2, -1])
        4

        >>> Solution().maxSubarraySumCircular([3, -2, 2, -3])
        3

        >>> Solution().maxSubarraySumCircular([-2, -3, -1])
        -1

        """

        mem = [0] * len(A)
        m_mem = [0] * len(A)
        for idx, val in enumerate(A):
            try:
                mem[idx] = max(val, val + mem[idx - 1])
            except IndexError:
                mem[idx] = val

            try:
                m_mem[idx] = min(val, val + m_mem[idx - 1])
            except IndexError:
                m_mem[idx] = val
        max_mem = max(mem)
        return max(max_mem, sum(A) - min(m_mem)) if max_mem > 0 else max_mem
