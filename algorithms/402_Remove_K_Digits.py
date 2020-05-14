class Solution(object):

    def removeKdigits(self, num, k):
        """
        Given a non-negative integer num represented as a string, remove k digits from the number so that the new number
        is the smallest possible.

        Note:
        The length of num is less than 10002 and will be ≥ k.
        The given num does not contain any leading zero.

        Runtime: 36 ms, faster than 77.11% of Python3 online submissions for Remove K Digits.
        Memory Usage: 13.9 MB, less than 22.22% of Python3 online submissions for Remove K Digits.


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
