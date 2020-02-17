class Solution(object):

    def reverseStr(self, s, k):
        """
        Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting
        from the start of the string. If there are less than k characters left, reverse all of them. If there are less
        than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as
        original.

        Runtime: 24 ms, faster than 93.86% of Python3 online submissions for Reverse String II.
        Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Reverse String II.


        Parameters
        ----------
        s : str

        k : int


        Returns
        -------
        ret : str

        """

        ret = ""
        for subseq in range(len(s) // (2 * k)):
            block = (s[subseq * 2 * k:(subseq + 1) * 2 * k])
            ret += block[k-1::-1] + block[k:]

        block_rem = len(s) % (2 * k)
        block = s[len(s) - block_rem:]
        if block_rem == 0:
            return ret
        else:
            return ret + block[k-1::-1] + block[k:]
