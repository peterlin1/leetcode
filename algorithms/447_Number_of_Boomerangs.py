class Solution(object):

    def numberOfBoomerangs(self, points):
        """
        Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such
        that the distance between i and j equals the distance between i and k (the order of the tuple matters).

        Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in
        the range [-10000, 10000] (inclusive).

        Runtime: 1560 ms, faster than 17.22% of Python3 online submissions for Number of Boomerangs.
        Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Number of Boomerangs.


        Parameters
        ----------
        points : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().numberOfBoomerangs([[0, 0], [1, 0], [2, 0]])
        2

        """

        def _distance_squared(pt1, pt2):
            return (pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2

        ret = 0
        for pt_i in points:
            mem = {}
            for pt_j in points:
                if pt_i == pt_j:
                    continue
                dis = _distance_squared(pt_i, pt_j)
                try:
                    mem[dis] += 1
                except KeyError:
                    mem[dis] = 1

            ret += sum(cnt * (cnt - 1) for cnt in mem.values())
        return ret

