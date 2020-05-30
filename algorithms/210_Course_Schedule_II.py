from collections import defaultdict


class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        """
        There are a total of n courses you have to take, labeled from 0 to n-1.

        Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is
        expressed as a pair: [0,1]

        Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should
        take to finish all courses.

        There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all
        courses, return an empty array.

        Note:
        The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a
        graph is represented.
        You may assume that there are no duplicate edges in the input prerequisites.

        Runtime: 104 ms, faster than 69.50% of Python3 online submissions for Course Schedule II.
        Memory Usage: 16.9 MB, less than 10.71% of Python3 online submissions for Course Schedule II.


        Parameters
        ----------
        numCourses : int

        prerequisites : list


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().findOrder(2,  [[1, 0]])
        [0, 1]

        >>> Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
        [0, 1, 2, 3]

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
                        return []
                ret.append(vertex)
            _restack[vertex] = False
            return True

        mem = defaultdict(list)
        ret = []
        for edge in prerequisites:
            mem[edge[1]].append(edge[0])

        _visited = [False] * numCourses
        _restack = [False] * numCourses

        for _vertex in range(numCourses):
            if not _iterate(_vertex):
                return []
        return ret[::-1]
