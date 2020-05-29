class Solution(object):

    def countBits(self, num):
        """
        Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of
        1's in their binary representation and return them as an array.

        Brian Kernighan’s Algorithm
        15 / 15 test cases passed.
        Status: Accepted
        Runtime: 128 ms
        Memory Usage: 20.6 MB


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
