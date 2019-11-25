class Solution(object):

    def isPowerOfThree(self, n):
        """
        Given an integer, write a function to determine if it is a power of three.

        Runtime: 88 ms, faster than 64.34% of Python3 online submissions for Power of Three.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Power of Three.


        Parameters
        ----------
        n : int


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().isPowerOfThree(27)
        True

        >>> Solution().isPowerOfThree(0)
        False

        >>> Solution().isPowerOfThree(45)
        False

        """

        # return n > 0 and (1162261467 % n == 0)
        if n is 0:
            return False
        if n is 1:
            return True
        if n % 3 is not 0:
            return False
        return self.isPowerOfThree(int(n / 3))
