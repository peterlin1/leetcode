import heapq


class Solution(object):

    def lastStoneWeight(self, stones):
        """
        We have a collection of stones, each stone has a positive integer weight.

        Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y
        with x <= y.  The result of this smash is:

        If x == y, both stones are totally destroyed;
        If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
        At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

        Note:
        1 <= stones.length <= 30
        1 <= stones[i] <= 1000

        70 / 70 test cases passed.
        Status: Accepted
        Runtime: 28 ms
        Memory Usage: 13.8 MB


        Parameters
        ----------
        stones : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().lastStoneWeight([2, 7, 4, 1, 8, 1])
        1

        """

        # Inverse values
        i_stones = [-val for val in stones]
        heapq.heapify(i_stones)

        while len(i_stones) > 1:
            heapq.heappush(i_stones, heapq.heappop(i_stones) - heapq.heappop(i_stones))

        return -i_stones[0]
