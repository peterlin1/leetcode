class Solution(object):

    mem = {0: 0, 1: 1}

    def fib(self, N):
        """
        The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each
        number is the sum of the two preceding ones, starting from 0 and 1. That is,


        Parameters
        ----------
        N : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().fib(4)
        3

        """

        try:
            return self.mem[N]
        except KeyError:
            self.mem[N] = self.fib(N - 1) + self.fib(N - 2)
            return self.mem[N]
