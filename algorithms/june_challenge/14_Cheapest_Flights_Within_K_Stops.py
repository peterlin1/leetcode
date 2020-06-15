from collections import defaultdict
import heapq


class Solution(object):

    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

        Now given all the cities and flights, together with starting city src and the destination dst, your task is to
        find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

        Constraints:
        The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
        The size of flights will be in range [0, n * (n - 1) / 2].
        The format of each flight will be (src, dst, price).
        The price of each flight will be in the range [1, 10000].
        k is in the range of [0, n - 1].
        There will not be any duplicated flights or self cycles.

        45 / 45 test cases passed.
        Status: Accepted
        Runtime: 92 ms
        Memory Usage: 19.5 MB


        Parameters
        ----------
        n : int

        flights : list

        src : int

        dst : int

        K : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1)
        200

        >>> Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0)
        500

        """

        mem = defaultdict(dict)

        for _src, _dst, price in flights:
            mem[_src][_dst] = price

        heap = [(0, src, K + 1)]

        while heap:
            price, city, k = heapq.heappop(heap)
            if city == dst:
                return price
            if k > 0:
                for _dst in mem[city]:
                    heapq.heappush(heap, (price + mem[city][_dst], _dst, k - 1))
        return -1
