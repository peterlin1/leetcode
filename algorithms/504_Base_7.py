class Solution(object):

    def convertToBase7(self, num):
        """
        Given an integer, return its base 7 string representation.

        Runtime: 24 ms, faster than 87.56% of Python3 online submissions for Base 7.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Base 7.


        Parameters
        ----------
        num : int


        Returns
        -------
        ret : str


        Examples
        --------
        >>> Solution().convertToBase7(100)
        "202"

        """

        if num is 0:
            return "0"
        ret = []
        c_num = abs(num)
        while c_num != 0:
            ret.insert(0, str(c_num % 7))
            c_num //= 7

        if num < 0:
            return "-" + "".join(ret)
        return "".join(ret)
