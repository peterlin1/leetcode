class StockSpanner():
    """
    Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's
    price for the current day.

    The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and
    going backwards) for which the price of the stock was less than or equal to today's price.

    For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans
    would be [1, 1, 1, 2, 1, 4, 6].

    Note:
    Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
    There will be at most 10000 calls to StockSpanner.next per test case.
    There will be at most 150000 calls to StockSpanner.next across all test cases.
    The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.


    99 / 99 test cases passed.
    Status: Accepted
    Runtime: 716 ms
    Memory Usage: 18.5 MB

    """

    def __init__(self):
        self.mem = []

    def next(self, price):
        """

        Parameters
        ----------
        price : int


        Returns
        -------
        ret : int

        """

        ret = 1
        while self.mem and price >= self.mem[-1][0]:
            ret += self.mem[-1][1]
            self.mem.pop()
        self.mem.append((price, ret))
        return ret


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
if __name__ == "__main__":
    ex1 = StockSpanner()
    ex1.next(100)
    ex1.next(80)
    ex1.next(60)
    ex1.next(70)
    ex1.next(60)
    ex1.next(75)
    ex1.next(85)
