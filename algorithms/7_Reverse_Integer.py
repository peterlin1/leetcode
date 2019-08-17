class Solution(object):

    def reverse(self, x):
        """
        Given a 32-bit signed integer, reverse digits of an integer.


        Parameters
        ----------
        x : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().reverse(123)
        321

        >>> Solution().reverse(-123)
        -321

        >>> Solution().reverse(120)
        21

        >>> Solution().reverse(1534236469)
        0

        """

        if x < 0:
            ret = -1*int(str(-x)[::-1])
        else:
            ret = int(str(x)[::-1])

        if (-1 << 31) < ret < (1 << 31):
            return ret
        else:
            return 0


