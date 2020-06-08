class Solution(object):

    def isPowerOfTwo(self, n):
        """
        Given an integer, write a function to determine if it is a power of two.

        Decrement and compare
        1108 / 1108 test cases passed.
        Status: Accepted
        Runtime: 24 ms
        Memory Usage: 13.8 MB


        Parameters
        ----------
        n : int


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().isPowerOfTwo(16)
        True

        >>> Solution().isPowerOfTwo(1)
        True

        >>> Solution().isPowerOfTwo(218)
        False

        """

        return (n != 0) and not (n & (n - 1))
