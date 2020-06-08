class Solution(object):

    def change(self, amount, coins):
        """
        You are given coins of different denominations and a total amount of money. Write a function to compute the
        number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

        Note:
        You can assume that
        0 <= amount <= 5000
        1 <= coin <= 5000
        the number of coins is less than 500
        the answer is guaranteed to fit into signed 32-bit integer

        27 / 27 test cases passed.
        Status: Accepted
        Runtime: 204 ms
        Memory Usage: 13.7 MB


        Parameters
        ----------
        amount : int

        coins : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().change(5, [1, 2, 5])
        4

        >>> Solution().change(3, [2])
        0

        >>> Solution().change(10, [10])
        1

        """

        mem = [0] * (amount + 1)
        mem[0] = 1
        for dem in coins:
            for val in range(1, amount + 1):
                if val >= dem:
                    mem[val] += mem[val - dem]
        return mem[-1]


if __name__ == "__main__":
    print(Solution().change(5, [1, 2, 5]))
