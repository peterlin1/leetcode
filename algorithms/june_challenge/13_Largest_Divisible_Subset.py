class Solution(object):

    def largestDivisibleSubset(self, nums):
        """
        Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in
        this subset satisfies:

        Si % Sj = 0 or Sj % Si = 0.

        If there are multiple solutions, return any subset is fine.

        41 / 41 test cases passed.
        Status: Accepted
        Runtime: 444 ms
        Memory Usage: 13.9 MB


        Parameters
        ----------
        nums : list

        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().largestDivisibleSubset([1, 2, 3]])
        [1, 2] or [1, 3]

        >>> Solution().largestDivisibleSubset([1, 2, 4, 8])
        [1, 2, 4, 8]

        """

        if len(nums) <= 1:
            return nums

        ret = []
        s_nums = sorted(nums)
        mem = [1] * len(nums)
        m_idx = 0

        for idx in range(1, len(nums)):
            for jdx in range(idx - 1, -1, -1):
                if s_nums[idx] % s_nums[jdx] == 0:
                    mem[idx] = max(mem[idx], mem[jdx] + 1)

            if mem[idx] > mem[m_idx]:
                m_idx = idx

        m_mem = mem[m_idx]
        idx = m_idx
        while m_mem > 0 and idx >= 0:
            if (s_nums[m_idx] % s_nums[idx] == 0) and (mem[idx] == m_mem):
                ret.append(s_nums[idx])
                m_mem -= 1
            idx -= 1

        return ret
