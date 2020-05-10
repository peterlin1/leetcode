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

        Runtime: 1092 ms, faster than 14.27% of Python3 online submissions for Find the Town Judge.
        Memory Usage: 18.3 MB, less than 10.00% of Python3 online submissions for Find the Town Judge.


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

        mem = {_: 0 for _ in range(1, N + 1)}
        for t in trust:
            try:
                mem[t[1]] += 1
            except KeyError:
                pass

            try:
                del mem[t[0]]
            except KeyError:
                pass

            if not mem:
                return -1

        for k in mem:
            if mem[k] == N - 1:
                return k
        return -1
