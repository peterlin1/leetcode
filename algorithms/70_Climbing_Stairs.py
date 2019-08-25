class Solution(object):
    mem = {1: 1, 2: 2}

    def climbStairs(self, n):
        """
        You are climbing a stair case. It takes n steps to reach to the top.

        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

        Note: Given n will be a positive integer.

        DP implementation with memoization. Essentially a shifted Fibonacci sequence.

        Runtime: 32 ms, faster than 89.12% of Python3 online submissions for Climbing Stairs.
        Memory Usage: 13.9 MB, less than 5.97% of Python3 online submissions for Climbing Stairs.


        Parameters
        ----------
        n : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().climbStairs(2)
        2

        >>> Solution().climbStairs(3)
        3

        >>> Solution().climbStairs(18)
        4181

        """
        # Try-clause faster than checking for key
        try:
            return self.mem[n]
        except KeyError:
            self.mem[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.mem[n]
