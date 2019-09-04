class Solution(object):

    def maxProfit(self, prices):
        """
        Say you have an array for which the ith element is the price of a given stock on day i.

        If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
        design an algorithm to find the maximum profit.

        Note that you cannot sell a stock before you buy one.

        Runtime: 68 ms, faster than 93.26% of Python3 online submissions for Best Time to Buy and Sell Stock.
        Memory Usage: 14.9 MB, less than 5.75% of Python3 online submissions for Best Time to Buy and Sell Stock.


        Parameters
        ----------
        prices : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().maxProfit([7, 1, 5, 3, 6, 4])
        5

        >>> Solution().maxProfit([7, 6, 4, 3, 1])
        0

        """

        ret = 0
        try:
            min_val = prices[0]
        except IndexError:
            return ret
        for idx in range(len(prices)):
            if prices[idx] > min_val:
                n_max = prices[idx] - min_val
                if n_max > ret:
                    ret = n_max
            else:
                min_val = prices[idx]
        return ret
