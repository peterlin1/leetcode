class Solution(object):

    def constructRectangle(self, area):
        """
        For a web developer, it is very important to know how to design a web page's size. So, given a specific
        rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W
        satisfy the following requirements:

        1. The area of the rectangular web page you designed must equal to the given target area.

        2. The width W should not be larger than the length L, which means L >= W.

        3. The difference between length L and width W should be as small as possible.
        You need to output the length L and the width W of the web page you designed in sequence.

        Note:
        The given area won't exceed 10,000,000 and is a positive integer
        The web page's width and length you designed must be positive integers.

        Runtime: 28 ms, faster than 78.71% of Python3 online submissions for Construct the Rectangle.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Construct the Rectangle.


        Parameters
        ----------
        area : int


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().constructRectangle(4)
        [2, 2]

        """

        # Adapted from 69 Sqrt to return approximation of sqrt of a given positive integer
        def _get_root(num):
            ret = num / 2
            while ret != num:
                n_ret = ret - (((ret ** 2) - num) / (2 * ret))
                if int(n_ret) == int(ret):
                    return int(ret)
                else:
                    ret = n_ret
            return int(area)

        for idx in range(_get_root(area), 0, -1):
            if area % idx is 0:
                return [area // idx, idx]
