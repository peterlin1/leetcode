class Solution(object):

    def countBits(self, num):
        """
        Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of
        1's in their binary representation and return them as an array.

        Brian Kernighan’s Algorithm
        Runtime: 140 ms, faster than 23.34% of Python3 online submissions for Counting Bits.
        Memory Usage: 20.7 MB, less than 5.00% of Python3 online submissions for Counting Bits.


        Parameters
        ----------
        num : int


        Returns
        -------
        ret : list

        """

        ret = [0]
        for val in range(1, num + 1):
            _bit = 0
            while val:
                # clear right-most set bit
                val &= (val - 1)
                _bit += 1
            ret.append(_bit)
        return ret

