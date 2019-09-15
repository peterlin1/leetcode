class Solution(object):

    def countPrimes(self, n):
        """
        Count the number of prime numbers less than a non-negative number, n.

        Runtime: 412 ms, faster than 73.70% of Python3 online submissions for Count Primes.
        Memory Usage: 25.4 MB, less than 79.31% of Python3 online submissions for Count Primes.


        Parameters
        ----------
        n : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().countPrimes(10)
        4

        """

        if n <= 1:
            return 0
        mem = [True] * n
        mem[0] = False
        mem[1] = False

        for sqr_n in range(2, int(n ** 0.5) + 1):
            if mem[sqr_n]:
                for multiple in range(sqr_n + sqr_n, n, sqr_n):
                    mem[multiple] = False

        return sum(mem)
