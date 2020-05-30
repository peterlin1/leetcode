from collections import defaultdict


class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        """
        There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

        Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is
        expressed as a pair: [0,1]

        Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all
        courses?

        Constraints:
        The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a
        graph is represented.
        You may assume that there are no duplicate edges in the input prerequisites.
        1 <= numCourses <= 10^5

        46 / 46 test cases passed.
        Status: Accepted
        Runtime: 104 ms
        Memory Usage: 16.9 MB


        Parameters
        ----------
        numCourses : int

        prerequisites : list


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().canFinish(2, [[1, 0]])
        True

        >>> Solution().canFinish(2, [[1, 0], [0, 1]])
        False

        """

        def _iterate(vertex):
            if not _visited[vertex]:
                _visited[vertex] = True
                _restack[vertex] = True
                for _adj_vertex in mem[vertex]:
                    if not _visited[_adj_vertex]:
                        if not _iterate(_adj_vertex):
                            return False
                    elif _restack[_adj_vertex]:
                        return False
            _restack[vertex] = False
            return True

        mem = defaultdict(list)
        for edge in prerequisites:
            mem[edge[1]].append(edge[0])

        _visited = [False] * numCourses
        _restack = [False] * numCourses

        for _vertex in range(numCourses):
            if not _iterate(_vertex):
                return False
        return True


if __name__ == "__main__":
    print(Solution().canFinish(10, [[1,0], [8,6], [8,2], [7,8], [2,9], [3,4],[7,9], [4,5], [3,8], [9,3], [6,9]]))
