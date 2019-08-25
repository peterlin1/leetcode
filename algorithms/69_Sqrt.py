class Solution(object):

    def mySqrt(self, x):
        """
        Implement int sqrt(int x).

        Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

        Since the return type is an integer, the decimal digits are truncated and only the integer part of the result
        is returned.

        Implementation of https://en.wikipedia.org/wiki/Newton%27s_method#Square_root_of_a_number

        Runtime: 40 ms, faster than 80.42% of Python3 online submissions for Sqrt(x).
        Memory Usage: 13.9 MB, less than 6.45% of Python3 online submissions for Sqrt(x).


        Parameters
        ----------
        x : int


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().mySqrt(8)
        2

        >>> Solution().mySqrt(612)
        24

        """

        ret = x/2
        while ret != x:
            n_ret = ret - (((ret ** 2) - x) / (2 * ret))
            if int(n_ret) == int(ret):
                return int(ret)
            else:
                ret = n_ret
        return int(ret)
