from collections import defaultdict


class Solution(object):

    def possibleBipartition(self, N, dislikes):
        """
        Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

        Each person may dislike some other people, and they should not go into the same group.

        Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same
        group.

        Return true if and only if it is possible to split everyone into two groups in this way.

        Note:
        1 <= N <= 2000
        0 <= dislikes.length <= 10000
        1 <= dislikes[i][j] <= N
        dislikes[i][0] < dislikes[i][1]
        There does not exist i != j for which dislikes[i] == dislikes[j].

        66 / 66 test cases passed.
        Status: Accepted
        Runtime: 880 ms
        Memory Usage: 22.3 MB


        Parameters
        ----------
        N : int

        dislikes : list


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().possibleBipartition(4, [[1, 2], [1, 3], [2, 4]])
        True

        >>> Solution().possibleBipartition(3, [[1, 2], [1, 3], [2, 3]])
        False

        >>> Solution().possibleBipartition(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]])
        False

        """

        def _iterate(idx, group):
            groups[idx] = group
            for _target in edges[idx + 1]:
                if groups[_target - 1] == group:
                    return False
                if (not groups[_target - 1]) and (not _iterate(_target - 1, group ^ 1)):
                    return False
            return True

        edges = defaultdict(list)
        for source, target in dislikes:
            edges[source].append(target)
            edges[target].append(source)

        groups = [None for _ in range(N)]

        for p_idx in range(N):
            if (not groups[p_idx]) and (not _iterate(p_idx, 0)):
                return False
        return True
