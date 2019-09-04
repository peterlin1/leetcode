class Solution(object):

    def maxProfit(self, prices):
        """
        Say you have an array for which the ith element is the price of a given stock on day i.

        Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one
        and sell one share of the stock multiple times).

        Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy
        again).

        Runtime: 68 ms, faster than 89.71% of Python3 online submissions for Best Time to Buy and Sell Stock II.
        Memory Usage: 14.7 MB, less than 7.32% of Python3 online submissions for Best Time to Buy and Sell Stock II.


        Parameters
        ----------
        prices : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().maxProfit([7, 1, 5, 3, 6, 4])
        7

        >>> Solution().maxProfit([1, 2, 3, 4, 5])
        4

        >>> Solution().maxProfit([7, 6, 4, 3, 1])
        0

        """

        ret = 0
        if len(prices) <= 1:
            return ret
        for idx in range(1, len(prices)):
            n_ret = prices[idx] - prices[idx - 1]
            if n_ret > 0:
                ret += n_ret
        return ret
