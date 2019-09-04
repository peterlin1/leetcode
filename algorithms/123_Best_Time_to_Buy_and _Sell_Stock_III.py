class Solution(object):

    def maxProfit(self, prices):
        """
        Say you have an array for which the ith element is the price of a given stock on day i.

        Design an algorithm to find the maximum profit. You may complete at most two transactions.

        Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

        Runtime: 92 ms, faster than 52.50% of Python3 online submissions for Best Time to Buy and Sell Stock III.
        Memory Usage: 14.8 MB, less than 63.64% of Python3 online submissions for Best Time to Buy and Sell Stock III.


        Parameters
        ----------
        prices : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
        6

        >>> Solution().maxProfit([1, 2, 3, 4, 5])
        4

        >>> Solution().maxProfit([7, 6, 4, 3, 1])
        0

        >>> Solution().maxProfit([3, 2, 6, 5, 0, 3])
        7

        """

        try:
            min_val = prices[0]
            max_val = prices[-1]
            mem_sell = [0] * len(prices)
            mem_buy = [0] * len(prices)
        except IndexError:
            return 0
        # Has to be done sequentially; can use negative indices instead though will require more arithmetic
        for idx in range(len(prices) - 2, -1, -1):
            mem_buy[idx] = max(max_val - prices[idx], mem_buy[idx + 1])
            if prices[idx] > max_val:
                max_val = prices[idx]
        ret = mem_buy[0]

        for idx in range(1, len(prices)):
            mem_sell[idx] = max(prices[idx] - min_val, mem_sell[idx - 1])
            if prices[idx] < min_val:
                min_val = prices[idx]

            # Max gain within two transactions at a given day is equal to max sell at given day + max buy at next day
            ret = max(ret, mem_sell[idx - 1] + mem_buy[idx])
        return ret
