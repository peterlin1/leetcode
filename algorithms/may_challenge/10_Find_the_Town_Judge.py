class Solution(object):

    def findJudge(self, N, trust):
        """
        In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the
        town judge.

        If the town judge exists, then:

        The town judge trusts nobody.
        Everybody (except for the town judge) trusts the town judge.
        There is exactly one person that satisfies properties 1 and 2.
        You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the
        person labelled b.

        If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

        Note:
        1 <= N <= 1000
        trust.length <= 10000
        trust[i] are all different
        trust[i][0] != trust[i][1]
        1 <= trust[i][0], trust[i][1] <= N

        89 / 89 test cases passed.
        Status: Accepted
        Runtime: 1160 ms
        Memory Usage: 18.3 MB


        Parameters
        ----------
        N : int

        trust : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().findJudge(2, [[1, 2]])
        2

        >>> Solution().findJudge(3, [[1, 3], [2, 3]])
        3

        >>> Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]])
        -1

        >>> Solution().findJudge(3, [[1, 2], [2, 3]])
        -1

        """

        mem = [0] * (N + 1)
        for t1, t2 in trust:
            mem[t2] += 1
            mem[t1] = 0

        for k in range(1, N + 1):
            if mem[k] == N - 1:
                return k
        return -1
