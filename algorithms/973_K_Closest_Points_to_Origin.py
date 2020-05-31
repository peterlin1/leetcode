import heapq
from math import hypot


class Solution(object):

    def kClosest(self, points, K):
        """
        We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

        (Here, the distance between two points on a plane is the Euclidean distance.)

        You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is
        in.)

        Note:
        1 <= K <= points.length <= 10000
        -10000 < points[i][0] < 10000
        -10000 < points[i][1] < 10000

        Runtime: 688 ms, faster than 82.70% of Python3 online submissions for K Closest Points to Origin.
        Memory Usage: 19.2 MB, less than 5.80% of Python3 online submissions for K Closest Points to Origin.


        Parameters
        ----------
        points : list

        K : int


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().kClosest([[1, 3], [-2, 2]], 1)
        [[-2,2]]

        >>> Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2)
         [[3, 3], [-2, 4]]
        """

        heap = []
        for point in points:
            if len(heap) < K:
                heapq.heappush(heap, (-hypot(point[0], point[1]), point))
            else:
                heapq.heappushpop(heap, (-hypot(point[0], point[1]), point))

        return [_[1] for _ in heap]
