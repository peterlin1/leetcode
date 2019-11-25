class Solution(object):

    def isPowerOfFour(self, num):
        """
        Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

        Runtime: 32 ms, faster than 84.40% of Python3 online submissions for Power of Four.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Power of Four.


        Parameters
        ----------
        num : int


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().isPowerOfFour(16)
        True

        >>> Solution().isPowerOfFour(5)
        False

        """

        if num < 1:
            return False
        if num is 1:
            return True
        # A power of 4 in binary contains an even number of 0 bits and 1 left-most 1 bit
        b_num = bin(num - 1).replace("0b", "")
        if "0" in b_num or (len(b_num) % 2 is not 0):
            return False
        return True
