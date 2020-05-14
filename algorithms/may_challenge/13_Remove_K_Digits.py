class Solution(object):

    def removeKdigits(self, num, k):
        """
        Given a non-negative integer num represented as a string, remove k digits from the number so that the new number
        is the smallest possible.

        Note:
        The length of num is less than 10002 and will be ≥ k.
        The given num does not contain any leading zero.

        33 / 33 test cases passed.
        Status: Accepted
        Runtime: 40 ms
        Memory Usage: 14 MB


        Parameters
        ----------
        num : str

        k : int


        Returns
        -------
        ret : str


        Examples
        --------
        >>> Solution().removeKdigits("1432219", 3)
        "1219"

        >>> Solution().removeKdigits("10200", 1)
        "200"

        >>> Solution().removeKdigits("10", 2)
        "0"

        """

        if len(num) == k:
            return "0"

        ret = ""

        for digit in num:
            while (k > 0) and ret and ret[-1] > digit:
                ret = ret[: -1]
                k -= 1
            if (not ret) and digit == '0':
                continue
            ret += digit
        while (k > 0) and ret:
            ret = ret[: -1]
            k -= 1
        return "0" if not ret else ret
