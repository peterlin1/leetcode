class Solution(object):

    def twoCitySchedCost(self, costs):
        """
        There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is
        costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

        Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

        Note:
        1 <= costs.length <= 100
        It is guaranteed that costs.length is even.
        1 <= costs[i][0], costs[i][1] <= 1000

        49 / 49 test cases passed.
        Status: Accepted
        Runtime: 36 ms
        Memory Usage: 13.7 MB


        Parameters
        ----------
        costs : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]])
        110

        """

        ret = 0
        l_costs = len(costs)

        diff_costs = [person[1] - person[0] for person in costs]
        sorted_costs = sorted(range(l_costs), key=lambda k: diff_costs[k])

        mid = (l_costs // 2)
        for idx in range(l_costs):
            ret += costs[sorted_costs[idx]][0] if idx >= mid else costs[sorted_costs[idx]][1]
        return ret
