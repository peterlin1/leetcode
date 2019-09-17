class Solution(object):

    def isPowerOfTwo(self, n):
        """
        Given an integer, write a function to determine if it is a power of two.

        Decrement and compare
        Runtime: 32 ms, faster than 95.53% of Python3 online submissions for Power of Two.
        Memory Usage: 13.7 MB, less than 9.52% of Python3 online submissions for Power of Two.


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
