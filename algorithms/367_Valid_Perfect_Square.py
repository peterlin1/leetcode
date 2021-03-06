class Solution(object):

    def isPerfectSquare(self, num):
        """
        Given a positive integer num, write a function which returns True if num is a perfect square else False.

        Note: Do not use any built-in library function such as sqrt.

        Adaptation of Problem 69: Sqrt
        Runtime: 20 ms, faster than 99.25% of Python3 online submissions for Valid Perfect Square.
        Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Valid Perfect Square.


        Parameters
        ----------
        num : int


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().isPerfectSquare(16)
        True

        >>> Solution().isPerfectSquare(14)
        False

        """

        ret = num / 2
        o_ret = 1
        while ret != num:
            n_ret = ret - (((ret ** 2) - num) / (2 * ret))
            # print(o_ret, ret, n_ret)
            if n_ret == o_ret:
                return False
            if n_ret == int(n_ret) == int(ret):
                return True
            o_ret = ret
            ret = n_ret
        return False
